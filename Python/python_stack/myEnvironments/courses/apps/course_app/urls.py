from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^add$', views.add),
    # the regex <id> is a parameter that needs to be passed. 
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
]
