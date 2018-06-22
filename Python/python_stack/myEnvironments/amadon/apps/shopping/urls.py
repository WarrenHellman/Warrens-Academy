from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
url(r'^$', views.index),
url(r'^buy$', views.buy),
url(r'^purchase$', views.purchase),
url(r'^clear$', views.clear)
]
