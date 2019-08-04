from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^random_word$', views.index),
    url(r'^generate_random_word$', views.randWord),
    url(r'^clear$', views.clear),

]