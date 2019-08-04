from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.signin),
    url(r'^signin$', views.signin),
    url(r'^processregistration$', views.processregister),
    url(r'^processlogin$', views.processlogin),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    ]