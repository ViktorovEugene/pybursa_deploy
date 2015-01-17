from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='pybursa/base.html'), name='home'),
    url(r'^students/', include('students.urls'), name='students'),
    url(r'^courses/', include('courses.urls'), name='courses'),
    url(r'^coaches/', include('coaches.urls'), name='coaches'),
    url(r'^address/', include('address.urls'), name='address'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
