from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page' : 'login'}, name='logout'),
)
