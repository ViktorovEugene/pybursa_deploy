from django.conf.urls import patterns, include, url
from coaches.views import (CoachesListView, CoachesDetailView, CoachesUpdateView, 
						  CoachesDeleteView, CoachesCreateView)


urlpatterns = patterns('',

    url(r'^$', CoachesListView.as_view(), name='coaches_list'),
    url(r'^new/$', CoachesCreateView.as_view(), name='coaches_new'),
    url(r'^(?P<pk>\d+)/$', CoachesDetailView.as_view(), name='coaches_item'),
    url(r'^edit/(?P<pk>\d+)/$', CoachesUpdateView.as_view(), name='coaches_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CoachesDeleteView.as_view(), name='coaches_delete'),


)
