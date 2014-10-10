from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    BaseUserManager
)

class MyUserManager(BaseUserManager):

    def create_superuser(self, email, password, tradeInProduct = None):
        """
        Creates and saves a superuser with the given email, password and product
        """
        if not tradeInProduct:
            tradeInProduct = TradeInProduct(
                name = "",
                description = "",
                price = 0,
                categories = Category(
                    "",
                    "",
                ),
            )
            tradeInProduct.save()

        user = self.create_user(email,
            password=password,
            tradeInProduct=tradeInProduct
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class TroccUser(AbstractUser):
    rating = models.PositiveSmallIntegerField(default=0)
    date_of_birth = models.DateField(auto_now_add=True)

    ''' Use the below manager when you will need additional super(user) data'''
    #objects = MyUserManager()

    def __unicode__(self):
        return self.username

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
    categories = models.ManyToManyField(Category, null=True)
    user = models.ForeignKey(TroccUser)

    def __unicode__(self):
       return self.name

class TradeInProduct(Product):
    tradeForProduct = models.ManyToManyField("TradeForProduct", null=True, blank=True, related_name='tradeForProducts')
    price = models.PositiveIntegerField()


class TradeForProduct(Product):
    tradeInPrice = models.PositiveIntegerField(null=True, default=0, editable=False, blank=True)

