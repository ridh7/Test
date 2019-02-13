from django.conf.urls import url
from . import views
app_name = 'basic'

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^(?P<question_id>[0-9])/$', views.question, name='question'),
]