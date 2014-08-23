from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
from blog.views import hello, current_url_view_good, getCities, index, initialize_database,indexcity,top_30_city,worst_30_city
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'air.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^path/$',current_url_view_good),
   # ('^getdata/$',getCities),
    #('^index/$',index),
    #('^register/$',reg),
    ('^init/$',initialize_database),
    #('^citydata',indexcity),
    url(r'^index','blog.views.index',name='regiondata'),
    url(r'^citydata','blog.views.indexcity',name='citydata'),
    url(r'^worst_30_city','blog.views.worst_30_city',name='worst_30_city'),
    url(r'^top_30_city','blog.views.top_30_city',name='top_30_city'),
    url(r'^$', 'blog.views.first_page',name='home'),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #                                         { 'document_root':settings.STATIC_ROOT }),

)
