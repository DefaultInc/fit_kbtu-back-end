from django.conf.urls import url

from tel.views import tel_create, TelList, tel_detail

urlpatterns = [
    url(r'^tels/create/$', tel_create),
    url(r'^tels/$', TelList.as_view()),
    url(r'^tels/(?P<pk>[0-9]+)/$', tel_detail),
]