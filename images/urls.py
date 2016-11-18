from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^get_all/$', views.get_all, name='get_all'),
    
    url(r'^get_image/$', views.get_image, name='get_image'),
    url(r'^get_image_obj/$', views.get_image_obj, name='get_image_obj'),
    url(r'^get_image_url/$', views.get_image_url, name='get_image_url'),
    
]
