from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns =  [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^close/$', views.close, name='close'),
    url(r'^view/(?P<project_id>\d+)/$', views.view, name='view'),
    url(r'^deleteMember/(?P<project_id>\d+)/$', views.deleteMember, name='deleteMember'),
    url(r'^addMember/(?P<project_id>\d+)/$', views.addMember, name='addMember'),
]
