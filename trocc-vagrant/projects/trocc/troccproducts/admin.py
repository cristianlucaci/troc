from django.contrib import admin
from .models import TradeInProduct
from .models import TradeForProduct
from .models import Category

# Register your models here.

class ProductInLine(admin.TabularInline):
    model = TradeInProduct


class TradeForProductsAdmin(admin.ModelAdmin):
    model = TradeForProduct


admin.site.register(TradeForProduct, TradeForProductsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model = Category


admin.site.register(Category, CategoryAdmin)