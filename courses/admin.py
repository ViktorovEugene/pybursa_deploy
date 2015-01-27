from django.contrib import admin
from django.db import models
from courses.models import Course
from courses.models import Group

from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_max_show_all = 20
    list_display = ['name', 'tecnology', 'enrollment_of_students', 'protect']
    list_display_links = ['name']
    list_filter = ['tecnology', 'protect']
    list_editable = ['protect']
    ordering = ['tecnology']
    search_fields = ['name']
    save_as = True
    save_on_top = True
    # fieldsets = [
    #         (None, {'fields': ['name', 'tecnology', 'slug',
    #                            'venue', 'coach', 'description', 'protect']}),
    #         ('Teachers', {'fields': ['assistant'],
    #                       'classes': ['collapse']}),
    # ]
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget},
    }
    radio_fields = {'tecnology': admin.HORIZONTAL}

    def enrollment_of_students(self, obj):
        return ('%s' % obj.student_set.count())

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	
	list_per_page = 10
	list_max_show_all = 20
	list_display = ['name', 'protect', 'enrollment_of_students', 'get_course']
	list_display_links = ['name']
	list_filter = ['protect']
	list_editable = ['protect']
	search_fields = ['name']
	save_as = True
	save_on_top = True

	def get_course(self, obj):
		courses = obj.course.name
		return courses

	def enrollment_of_students(self, obj):
		return ('%s' % obj.student_set.count())