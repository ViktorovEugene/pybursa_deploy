from django.conf.urls import patterns, include, url
from address.views import (AddressListView, AddressDetailView, AddressUpdateView, 
						  AddressDeleteView, AddressCreateView)


urlpatterns = patterns('',

    url(r'^$', AddressListView.as_view(), name='address_list'),
    url(r'^new/$', AddressCreateView.as_view(), name='address_new'),
    url(r'^(?P<pk>\d+)/$', AddressDetailView.as_view(), name='address_item'),
    url(r'^edit/(?P<pk>\d+)/$', AddressUpdateView.as_view(), name='address_edit'),
    url(r'^delete/(?P<pk>\d+)/$', AddressDeleteView.as_view(), name='address_delete'),

)
