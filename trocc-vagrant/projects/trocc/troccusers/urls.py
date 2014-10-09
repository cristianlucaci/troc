__author__ = 'marianlungu'
from django.conf.urls import patterns, url
from .views import LoginUser

urlpatterns = patterns(
    'troccusers.views',
    url(r'^$/?$', 'index'),
    url(r'^login/?$', LoginUser.as_view()),
    url(r'^register/?$', 'sign_up'),
    url(r'^my_products/?$', 'my_products'),
    url(r'^logout/?$', 'logout_user'),
)
