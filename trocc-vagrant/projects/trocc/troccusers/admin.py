from django.contrib import admin

# Register your models here.
from .models import TroccUser
from troccproducts.admin import ProductInLine
from .forms import UserCreationForm

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


