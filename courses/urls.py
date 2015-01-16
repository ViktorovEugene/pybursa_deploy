from django.conf.urls import patterns, include, url
from courses.views import (CoursesListView, CoursesDetailView, CoursesUpdateView, 
						  CoursesDeleteView, CoursesCreateView)


urlpatterns = patterns('',

    url(r'^$', CoursesListView.as_view(), name='courses_list'),
    url(r'^(?P<pk>\d+)/$', CoursesDetailView.as_view(), name='courses_item'),
    url(r'^new/$', CoursesCreateView.as_view(), name='courses_new'),
    url(r'^edit/(?P<pk>\d+)/$', CoursesUpdateView.as_view(), name='courses_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CoursesDeleteView.as_view(), name='courses_delete'),

)
