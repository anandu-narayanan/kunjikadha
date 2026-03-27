"""
URL configuration for the story app.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Home page - story creation form
    path('', views.home, name='home'),
    
    # Story display page
    path('story/<uuid:session_id>/', views.story_detail, name='story_detail'),
    
    # API endpoint for continuing story
    path('api/story/<uuid:session_id>/continue/', views.continue_story_view, name='continue_story'),
    
    # Start new story
    path('new/', views.new_story, name='new_story'),
    
    # View all saved stories
    path('all-stories/', views.all_stories, name='all_stories'),
]
