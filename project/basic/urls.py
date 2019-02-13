from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'basic'

urlpatterns = [
    url(r'^basic/$', views.register, name='register'),
    url(r'^basic/(?P<question_id>[0-9])/$', views.question, name='question'),
    url(r'^basic/oops/$', views.index, name='index'),
    path('', views.welcome)
]
