from django.contrib import admin

# Register your models here.
from .models import TroccUser
from .models import TradeInProduct
from .models import TradeForProduct
from .models import Category
from .forms import UserCreationForm

class ProductInLine(admin.TabularInline):
    model = TradeInProduct

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]

class UserAdmin(admin.ModelAdmin):
    #model = TroccUser
    inlines = [
            ProductInLine,
        ]
    form = UserCreationForm
    list_display = ("username",)
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active')}
            ),
        )

    filter_horizontal = ()

admin.site.register(TroccUser, UserAdmin)

class TradeForProductsAdmin(admin.ModelAdmin):
    model = TradeForProduct


admin.site.register(TradeForProduct, TradeForProductsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model = Category


admin.site.register(Category, CategoryAdmin)

