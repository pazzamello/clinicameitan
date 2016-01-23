from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'clinicaMeiTan.views.home', name='home'),
    url(r'^$',"agenda.views.lista" ),
    url(r'^adiciona/$',"agenda.views.adiciona" ),
    url(r'^item/(?P<nr_item>\d+)/$', "agenda.views.item"),
    url(r'^remove/(?P<nr_item>\d+)/$', "agenda.views.remove"),
    url(r'^login/$', "django.contrib.auth.views.login", {
	    "template_name": "login.html" }),
    url(r'^logout/$', "django.contrib.auth.views.logout_then_login", {
	    "login_url": "/login/" }), 

    # url(r'^clinicaMeiTan/', include('clinicaMeiTan.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)
