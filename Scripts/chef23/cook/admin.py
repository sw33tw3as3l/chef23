from django.contrib import admin
from .models import GraphProject

# Register your models here.
@admin.register(GraphProject)
class GraphProjectAdmin(admin.ModelAdmin):

    list_display = ['owner', 'project_name', 'is_public']
    search_fields = ['project_name', 'owner__username']
    date_hierarchy = "pub_date"