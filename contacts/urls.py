from django.conf.urls import url
from .views import *

# main URL file for Contacts app. which redirects to the corresponding page

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^sendMessage/(\d+)/$', sendMessage, name='sendMessage'),
    url(r'^sent/$', sent, name='sent'),
    url(r'^test/$', test, name='test'),
]