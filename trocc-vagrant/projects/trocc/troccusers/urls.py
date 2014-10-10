__author__ = 'marianlungu'
from django.conf.urls import patterns, url
from .views import LoginUserView, SignUpView, MyProductsView

urlpatterns = patterns(
    'troccusers.views',
    url(r'^$/?$', 'index'),
    url(r'^login/?$', LoginUserView.as_view()),
    url(r'^register/?$', SignUpView.as_view()),
    url(r'^my_products/?$', MyProductsView.as_view()),
    url(r'^logout/?$', 'logout_user'),
)
