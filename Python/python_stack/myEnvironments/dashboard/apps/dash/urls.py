from django.conf.urls import url
from . import views  
urlpatterns = [
url(r'^$', views.index),
url(r'^signin$', views.signin),
url(r'^register$', views.register),
url(r'^dashboard$', views.dashboard),
url(r'^newUser$', views.newUser),
url(r'^passcheck$', views.passcheck),
url(r'^dashboard/admin$', views.dashAdmin),
url(r'^users/edit/(?P<id>\d+)$', views.edit),
url(r'^update/(?P<id>\d+)$', views.update),
url(r'^remove/(?P<id>\d+)$', views.remove),
]
