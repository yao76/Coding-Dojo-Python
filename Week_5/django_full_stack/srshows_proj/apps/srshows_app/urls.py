from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.index),
    url(r'^allshows$', views.index),
    url(r'^shows/new$', views.new),
    url(r'^shows/(?P<show_id>\d+)$', views.displayshowinfo),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.delete),

]