from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users$', views.index),
    url(r'^login$', views.login),
    url(r'^users/new$', views.new),
    url(r'^register$', views.new)
]


# /register - display 'placeholder for users to create a new user record'
# /login - display 'placeholder for users to login' 
# /users/new - have the same method that handles /register also handle the url request of /users/new
