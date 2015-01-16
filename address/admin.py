# -*- coding: utf-8 -*-
from django.contrib import admin
from address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_max_show_all = 20
    list_display = ['country', 'get_course']

    def get_course(self, obj):
		courses = obj.course_venue.values_list('name', flat=True)
		return ('%s' % (u", ".join(courses)))