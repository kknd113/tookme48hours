from django.conf.urls import patterns, include, url
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('help.views',
    # Examples:
    # url(r'^$', 'warm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'mainView'),
    url(r'^users/login', 'loginView'),
    url(r'^users/add', 'addView'),
    url(r'^TESTAPI/resetFixture', 'resetFixture'),
    url(r'^TESTAPI/unitTests', 'unitTests'),
)