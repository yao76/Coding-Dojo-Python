from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^wall$', views.success),
    url(r'^logout$', views.logout),
    url(r'^addmessage$', views.processmessage),
    url(r'^addcomment$', views.processcomment),
    url(r'^deletemessage$', views.deletemessage),
]