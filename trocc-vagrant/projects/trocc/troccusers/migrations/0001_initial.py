# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TroccUser'
        db.create_table(u'troccusers_troccuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'troccusers', ['TroccUser'])

        # Adding M2M table for field groups on 'TroccUser'
        m2m_table_name = db.shorten_name(u'troccusers_troccuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('troccuser', models.ForeignKey(orm[u'troccusers.troccuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['troccuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'TroccUser'
        m2m_table_name = db.shorten_name(u'troccusers_troccuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('troccuser', models.ForeignKey(orm[u'troccusers.troccuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['troccuser_id', 'permission_id'])

        # Adding model 'Category'
        db.create_table(u'troccusers_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoryName', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('fullDescription', self.gf('django.db.models.fields.CharField')(max_length=2550, null=True, blank=True)),
        ))
        db.send_create_signal(u'troccusers', ['Category'])

        # Adding model 'TradeInProduct'
        db.create_table(u'troccusers_tradeinproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2550, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['troccusers.TroccUser'])),
            ('price', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'troccusers', ['TradeInProduct'])

        # Adding M2M table for field categories on 'TradeInProduct'
        m2m_table_name = db.shorten_name(u'troccusers_tradeinproduct_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tradeinproduct', models.ForeignKey(orm[u'troccusers.tradeinproduct'], null=False)),
            ('category', models.ForeignKey(orm[u'troccusers.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tradeinproduct_id', 'category_id'])

        # Adding M2M table for field tradeForProducts on 'TradeInProduct'
        m2m_table_name = db.shorten_name(u'troccusers_tradeinproduct_tradeForProducts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tradeinproduct', models.ForeignKey(orm[u'troccusers.tradeinproduct'], null=False)),
            ('tradeforproduct', models.ForeignKey(orm[u'troccusers.tradeforproduct'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tradeinproduct_id', 'tradeforproduct_id'])

        # Adding model 'TradeForProduct'
        db.create_table(u'troccusers_tradeforproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2550, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['troccusers.TroccUser'])),
            ('tradeInPrice', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'troccusers', ['TradeForProduct'])

        # Adding M2M table for field categories on 'TradeForProduct'
        m2m_table_name = db.shorten_name(u'troccusers_tradeforproduct_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tradeforproduct', models.ForeignKey(orm[u'troccusers.tradeforproduct'], null=False)),
            ('category', models.ForeignKey(orm[u'troccusers.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tradeforproduct_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'TroccUser'
        db.delete_table(u'troccusers_troccuser')

        # Removing M2M table for field groups on 'TroccUser'
        db.delete_table(db.shorten_name(u'troccusers_troccuser_groups'))

        # Removing M2M table for field user_permissions on 'TroccUser'
        db.delete_table(db.shorten_name(u'troccusers_troccuser_user_permissions'))

        # Deleting model 'Category'
        db.delete_table(u'troccusers_category')

        # Deleting model 'TradeInProduct'
        db.delete_table(u'troccusers_tradeinproduct')

        # Removing M2M table for field categories on 'TradeInProduct'
        db.delete_table(db.shorten_name(u'troccusers_tradeinproduct_categories'))

        # Removing M2M table for field tradeForProducts on 'TradeInProduct'
        db.delete_table(db.shorten_name(u'troccusers_tradeinproduct_tradeForProducts'))

        # Deleting model 'TradeForProduct'
        db.delete_table(u'troccusers_tradeforproduct')

        # Removing M2M table for field categories on 'TradeForProduct'
        db.delete_table(db.shorten_name(u'troccusers_tradeforproduct_categories'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'troccusers.category': {
            'Meta': {'object_name': 'Category'},
            'categoryName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'fullDescription': ('django.db.models.fields.CharField', [], {'max_length': '2550', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'troccusers.tradeforproduct': {
            'Meta': {'object_name': 'TradeForProduct'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['troccusers.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2550', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tradeInPrice': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['troccusers.TroccUser']"})
        },
        u'troccusers.tradeinproduct': {
            'Meta': {'object_name': 'TradeInProduct'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['troccusers.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2550', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tradeForProducts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tradeInProducts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['troccusers.TradeForProduct']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['troccusers.TroccUser']"})
        },
        u'troccusers.troccuser': {
            'Meta': {'object_name': 'TroccUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['troccusers']