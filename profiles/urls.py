from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns =  [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^resetpassword/$', views.resetpassword, name='resetpassword'),
]
