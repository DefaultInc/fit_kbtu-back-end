from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from authentication.views import register, user_profile, get_user_info

urlpatterns = [
    url(r'register/', register),
    url(r'^login/', obtain_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    url(r'user/$', user_profile),
    url(r'user/(?P<pk>[0-9]+)/$', get_user_info),
]
