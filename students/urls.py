from django.conf.urls import patterns, url
from students.views import (StudentsListView, StudentsDetailView, StudentsUpdateView, 
						  StudentsDeleteView, StudentsCreateView)

urlpatterns = patterns('',

    url(r'^$', StudentsListView.as_view(), name='students_list'),
    url(r'^(?P<pk>\d+)/$', StudentsDetailView.as_view(), name='students_item'),
    url(r'^new/$', StudentsCreateView.as_view(), name='students_new'),
    url(r'^edit/(?P<pk>\d+)/$', StudentsUpdateView.as_view(), name='students_edit'),
    url(r'^delete/(?P<pk>\d+)/$', StudentsDeleteView.as_view(), name='students_delete'),
)
