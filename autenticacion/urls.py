__author__ = 'alforro'

from django.conf.urls import patterns, url
from autenticacion import views

urlpatterns = patterns('',
url(r'^$', views.index, name='index'),
url(r'^logout_nuevo/$', views.logout_view, name='logout' ),
)
