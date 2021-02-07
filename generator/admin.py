from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdminView(admin.ModelAdmin):
    list_display = ['email', 'active', 'count', 'slug', 'created', 'updated']
    list_filter = ['active', 'count']
    sortable_by = ['active', 'count', 'created', 'updated']
