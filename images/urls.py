from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^get_all/$', views.get_all, name='get_all'),
    url(r'^get_image/(?P<image_id>[0-9]+)/$', views.get_image, name='get_image'),
    
]
