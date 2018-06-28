from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success/register/(?P<id>\d+)$', views.success),
    url(r'^login$', views.login),
    url(r'^success/login/(?P<id>\d+)$', views.success)
]

