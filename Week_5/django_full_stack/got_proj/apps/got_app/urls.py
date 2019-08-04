from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^dashboard$', views.success),
    url(r'^logout$', views.logout),
    url(r'^processnewevent$', views.processnewevent),
    url(r'^processeditevent/(?P<event_id>\d+)$', views.processeditevent),
    url(r'^updateevent/(?P<event_id>\d+)$', views.updateevent),
    url(r'^new-event$', views.newevent),
    url(r'^events/(?P<event_id>\d+)/edit$', views.updateevent),
    url(r'^events/(?P<event_id>\d+)$', views.eventinfo),
    url(r'^events$', views.events),
    url(r'^processjoin/(?P<event_id>\d+)$', views.processjoin),
    url(r'^processcancel/(?P<event_id>\d+)$', views.processcancel),
    ]