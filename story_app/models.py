"""
Database models for the story app.
Stores story sessions and their content.
"""
from django.db import models
import uuid


class StorySession(models.Model):
    """
    Stores a story session with character, place, theme, and generated story content.
    """
    # Unique identifier for the session
    session_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    # User inputs
    character = models.CharField(max_length=100, help_text="Malayalam character name")
    place = models.CharField(max_length=100, help_text="Malayalam place name")
    theme = models.CharField(max_length=100, help_text="Story theme (e.g., friendship, kindness)")
    
    # Generated story content (stored as JSON string for flexibility)
    story_text = models.TextField(help_text="Generated story content")
    
    # Story history (to maintain continuity)
    story_history = models.JSONField(default=list, help_text="List of story parts for context")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Story Session'
        verbose_name_plural = 'Story Sessions'
    
    def __str__(self):
        return f"Story: {self.character} @ {self.place} - {self.theme}"
