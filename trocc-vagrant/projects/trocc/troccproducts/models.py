from django.db import models
from troccusers.models  import TroccUser

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=255, unique=True)
    fullDescription = models.CharField(max_length= 255 * 10, null=True, blank=True)

    def __unicode__(self):
        return self.categoryName

class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255 * 10, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(TroccUser)

    def __unicode__(self):
       return self.name

class TradeInProduct(Product):
    tradeForProducts = models.ManyToManyField("TradeForProduct", null=True, blank=True, related_name='tradeInProducts')
    price = models.PositiveIntegerField()


class TradeForProduct(Product):
    tradeInPrice = models.PositiveIntegerField(null=True, default=0, editable=False, blank=True)
