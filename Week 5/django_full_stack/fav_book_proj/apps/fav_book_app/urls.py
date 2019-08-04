from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^processaddbook$', views.processaddbook),
    url(r'^updatebook/(?P<book_id>\d+)$', views.updatebook),
    url(r'^deletebook/(?P<book_id>\d+)$', views.deletebook),
    url(r'^deletefavorite/(?P<book_id>\d+)$', views.deletefavorite),
    url(r'^addfavorite/(?P<book_id>\d+)$', views.addfavorite),
    url(r'^addfavoritemain/(?P<book_id>\d+)$', views.addfavoritemain),
    url(r'^books/(?P<book_id>\d+)$', views.displaybookinfo),
    url(r'^books$', views.success),
    url(r'^logout$', views.logout),
    ]