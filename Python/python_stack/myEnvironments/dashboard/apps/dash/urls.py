from django.conf.urls import url
from . import views  
urlpatterns = [
url(r'^$', views.index),
url(r'^signin$', views.signin),
url(r'^register$', views.register),
url(r'^dashboard$', views.dashboard),
]