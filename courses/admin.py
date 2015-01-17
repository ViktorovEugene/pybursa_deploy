from django.contrib import admin
from django.db import models
from courses.models import Course

from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_max_show_all = 20
    list_display = ['name', 'tecnology', 'start_date', 'end_date']
    list_display_links = ['name' , 'tecnology']
    ordering = ['tecnology']
    list_filter = ['tecnology', 'start_date', 'end_date']
    search_fields = ['name']
    save_as = True
    save_on_top = True
    fieldsets = [
            (None, {'fields': ['name', 'tecnology', 'slug',
                               'start_date', 'end_date',
                               'venue', 'coach', 'description']}),
            ('Teachers', {'fields': ['assistant'],
                          'classes': ['collapse']}),
    ]
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget},
    }
    radio_fields = {'tecnology': admin.HORIZONTAL}
    prepopulated_fields = {'slug': ('name',)}

