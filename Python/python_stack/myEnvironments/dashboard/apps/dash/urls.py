from django.conf.urls import url
from . import views

# All of the routes for the dashboard project
urlpatterns = [
url(r'^$', views.index),
url(r'^signin$', views.signin),
url(r'^register$', views.register),
url(r'^dashboard$', views.dashboard),
url(r'^newUser$', views.newUser),
url(r'^passcheck$', views.passcheck),
# The regex saves user ids and can pass them to our logic in views
url(r'^users/edit/(?P<id>\d+)$', views.edit),
url(r'^update/(?P<id>\d+)$', views.update),
url(r'^remove/(?P<id>\d+)$', views.remove),
url(r'^updatepwd/(?P<id>\d+)$', views.updatepwd),
url(r'^users/new$', views.add),
url(r'^addUser$', views.addUser),
url(r'^users/edituser/(?P<id>\d+)$', views.editUser),
url(r'^description/(?P<id>\d+)$', views.description),
url(r'^users/show/(?P<id>\d+)$', views.userpage),
url(r'^postmsg/(?P<id>\d+)$', views.postmsg),
url(r'^post-comment/(?P<id>\d+)$', views.postcomment),
]
