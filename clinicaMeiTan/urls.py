from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from agenda import views
from django.contrib.auth.views import logout_then_login, login
from django.views.generic.base import TemplateView
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^agenda/', include('agenda.urls')),
	url(r'^login/$',login, {"template_name": "login.html"}),
	url(r'^logout/$',logout_then_login, {"login_url": "/login/"}),
	url(r'^admin/',include(admin.site.urls)), 
	]

if settings.DEBUG:
	urlpatterns += [
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	]
