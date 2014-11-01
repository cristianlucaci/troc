__author__ = 'marianlungu'
from django.conf.urls import patterns, url
from views import MyProductsView

urlpatterns = patterns(
    'troccproducts.views',
     url(r'^my_products/?$', 'myProducts', name="products"),
)
