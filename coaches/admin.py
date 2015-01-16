from django.contrib import admin
from coaches.models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    radio_fields = {'status': admin.VERTICAL}
    list_display = ['status', 'name', 'surname',]
    list_display_links = ['status']
    list_per_page = 10
    list_max_show_all = 20
    ordering = ['status']
    list_filter = ['status']
    search_fields = ['name']

