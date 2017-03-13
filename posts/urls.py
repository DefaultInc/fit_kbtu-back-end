from django.conf.urls import url
from .views import post_list, post_detail

urlpatterns = [
    url(r'^posts/$', post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', post_detail),
]