from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
from blog.views import hello, current_url_view_good, getCities, index, reg
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TonyChol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^path/$',current_url_view_good),
    ('^getdata/$',getCities),
    ('^index/$',index),
    ('^register/$',reg),
    url(r'^$', 'blog.views.first_page'),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #                                         { 'document_root':settings.STATIC_ROOT }),

)
