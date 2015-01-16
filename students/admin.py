from django.contrib import admin
from students.models import Student
from students.models import Group

from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets

class StudentInline(admin.StackedInline):
    model = Student
    fk_name = 'group'
    fields = ['package']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_birth'
    filter_horizontal = ['courses']
    radio_fields = {'package': admin.VERTICAL}
    list_display = ['name','surname', 'package']
    list_display_links = ['name']
    list_per_page = 10
    list_max_show_all = 20
    ordering = ['package']
    list_filter = ['package', 'courses', 'courses__start_date']
    search_fields = ['name']
    list_editable = ['surname']
