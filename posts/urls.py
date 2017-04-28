from django.conf.urls import url
from .views import post_list, post_detail, comment_create, like_post, like_exists, get_all_pictures, post_create, \
    PostList

urlpatterns = [
    url(r'^posts/create/$', post_create),
    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', post_detail),
    url(r'^comments/$', comment_create),
    url(r'^like/$', like_post),
    url(r'^pictures/$', get_all_pictures),
]
