from django.conf.urls import url
from .views import post_list, post_detail, comment_create, like_post

urlpatterns = [
    url(r'^posts/$', post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', post_detail),
    url(r'^comments/$', comment_create),
    url(r'^like/$', like_post),
]