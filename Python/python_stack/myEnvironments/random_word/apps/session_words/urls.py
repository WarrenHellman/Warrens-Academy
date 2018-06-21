from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
url(r'^session_words$', views.load) ,
url(r'^session_words/process$', views.process),
url(r'^session_words/results$', views.results),
url(r'^session_words/clear$', views.clear)
]

