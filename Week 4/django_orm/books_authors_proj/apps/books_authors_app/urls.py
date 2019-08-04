from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addbook$', views.addbook),
    url(r'^books/(?P<num>\d+)$', views.bookinfo),
    url(r'^books/(?P<num>\d+)/update$', views.addauthortobook),
    url(r'^authors/(?P<num>\d+)$', views.authorinfo),
    url(r'^allauthors$', views.authorindex),
    url(r'^addauthors$', views.addauthor),
    url(r'^authors/(?P<num>\d+)/update$', views.addbooktoauthor),
    url(r'^delete$', views.deletebook),
]