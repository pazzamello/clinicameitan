from django.conf.urls import patterns, include, url

from agenda import views


urlpatterns = [
	url(r'^lista/$',views.lista),
	url(r'^adiciona/$',views.adiciona),
	url(r'^item/(?P<nr_item>\d+)/$',views.item),
	url(r'^remove/(?P<nr_item>\d+)/$',views.remove),
	]
