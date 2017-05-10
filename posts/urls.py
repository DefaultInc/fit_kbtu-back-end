from django.conf.urls import url
from .views import post_detail, comment_create, like_post, like_exists, post_create, \
    PostList, PostByTag, TagList, PostByTags

urlpatterns = [
    url(r'^posts/create/$', post_create),
    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', post_detail),
    url(r'^comments/$', comment_create),
    url(r'^like/$', like_post),
    url(r'posts_by_tag/(?P<pk>[0-9]+)/$', PostByTag.as_view()),
    url(r'tags/$', PostByTags.as_view()),
    # url(r'tags/(?P<pk>[0-9]+)/$', PostByTags.as_view()),
]
