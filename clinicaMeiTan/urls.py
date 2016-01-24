from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from agenda import views
from django.contrib.auth.views import logout_then_login, login
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
	url(r'^$',views.lista),
	url(r'^adiciona/$',views.adiciona),
	url(r'^item/(?P<nr_item>\d+)/$',views.item),
	url(r'^remove/(?P<nr_item>\d+)/$',views.remove),
	url(r'^login/$',login, {"template_name": "login.html"}),
	url(r'^logout/$',logout_then_login, {"login_url": "/login/"}),
	url(r'^admin/',include(admin.site.urls)), 
	]

if settings.DEBUG:
	urlpatterns += [
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	]
