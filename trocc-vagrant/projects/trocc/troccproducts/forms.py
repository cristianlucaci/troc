__author__ = 'marianlungu'
from models import Category, TradeInProduct, TradeForProduct
from django import forms

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