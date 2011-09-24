from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'leadin.views.home', name='home'),
#    url(r'keyword/(.*)', 'keywordgrader.views.keyword', name='keyword'),
)

urlpatterns += staticfiles_urlpatterns()
