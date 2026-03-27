from django.contrib import admin
from .models import StorySession


@admin.register(StorySession)
class StorySessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'character', 'place', 'theme')
    readonly_fields = ('created_at', 'updated_at', 'session_id')
    fields = ('session_id', 'character', 'place', 'theme', 'story_text', 'created_at', 'updated_at')
