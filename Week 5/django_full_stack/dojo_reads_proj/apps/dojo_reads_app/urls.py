from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^books$', views.success),
    url(r'^add$', views.addbook),
    url(r'^deletereview/(?P<review_id>\d+)$', views.deletereview),
    url(r'^processaddbook$', views.processaddbook),
    url(r'^books/(?P<book_id>\d+)$', views.displaybookinfo),
    url(r'^books/(?P<book_id>\d+)/add$', views.addreview),
    url(r'^users/(?P<user_id>\d+)$', views.displayuserinfo),
    url(r'^logout$', views.logout),
    ]