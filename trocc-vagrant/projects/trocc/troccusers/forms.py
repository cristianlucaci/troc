__author__ = 'marianlungu'
from django import forms
from .models import (
    TroccUser, TradeInProduct, TradeForProduct, Category
)
from . import log

class TroccUserForm(forms.ModelForm):
    class Meta:
        model = TroccUser
        fields = ('username', 'password')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryName', 'fullDescription',)

class TradeInProductForm(forms.ModelForm):
    class Meta:
        model = TradeInProduct
        fields = ('name', 'description', 'categories', 'price',)

    def save(self, user = None, commit=True):
        product = super(TradeInProductForm, self).save(commit=False)
        product.user = user
        if commit:
            product.save()
        return product


class TradeForProductForm(forms.ModelForm):
    class Meta:
        model = TradeForProduct

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = TroccUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        log.debug("Saving user")
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

