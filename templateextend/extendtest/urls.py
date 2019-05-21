from django.conf.urls import url
from . import views
app_name = 'extendtest'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/$', views.index, name='index')
]