from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]