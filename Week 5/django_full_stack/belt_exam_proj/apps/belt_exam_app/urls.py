from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^trips/edit/(?P<trip_id>\d+)$', views.edittrip),
    url(r'^processedittrip/(?P<trip_id>\d+)$', views.processedittrip),
    url(r'^trips/(?P<trip_id>\d+)/remove$', views.removetrip),
    url(r'^trips/(?P<trip_id>\d+)/cancel$', views.canceltrip),
    url(r'^trips/(?P<trip_id>\d+)$', views.displaytripinfo),
    url(r'^processnewtrip$', views.processnewtrip),
    url(r'^trips/new$', views.newtrip),
    url(r'^processjoin/(?P<trip_id>\d+)$', views.processjoin),
    ]