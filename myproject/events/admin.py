from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    search_fields = ('title',)