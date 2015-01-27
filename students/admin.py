from django.db import models
from django.contrib import admin
from students.models import Student
from courses.models import Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('protect', 'name', 'surname', 'date_of_birth',
             'email', 'phone', 'package', 'group')
    date_hierarchy = 'date_of_birth'
    filter_horizontal = ['group', 'courses']
    radio_fields = {'package': admin.VERTICAL}
    list_display = ['name','surname', 'groups', 'package', 
        'protect', 'item_courses']
    list_display_links = ['name']
    list_per_page = 10
    list_max_show_all = 20
    ordering = ['package']
    list_filter = ['package', 'group']
    search_fields = ['name']
    list_editable = ['surname', 'protect']
    
    def groups(self, obj):
        return ('%s' % (', '.join([ group.name for group in obj.group.all()])))

    # def get_courses(self, obj):
    #     obj.get_courses()
    #     return ('%s' % (
    #         ', '.join(
    #         [ Course.objects.get(pk=course_id[0]).name for course_id in obj.group.values_list('course_id').distinct()])
    #     ))

    def item_courses(self, obj):
        return ('%s' % (', '.join([course.name for course in obj.courses.all()])))