from django.conf.urls import patterns, include, url
from help.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', mainView),
)
