"""
Views for the story generation app.
Handles home page, story generation, and story continuation.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import uuid

from .models import StorySession
from .forms import StoryInitiationForm, StoryChoiceForm
from .utils import generate_initial_story, continue_story


def home(request):
    """
    Home page view - displays the story creation form.
    GET: Show the form
    POST: Create a new story session
    """
    if request.method == 'POST':
        form = StoryInitiationForm(request.POST)
        if form.is_valid():
            # Get form data
            character = form.cleaned_data['character']
            place = form.cleaned_data['place']
            theme = form.cleaned_data['theme']
            
            try:
                # Generate initial story
                story_data = generate_initial_story(character, place, theme)
                
                # Create story session
                session = StorySession.objects.create(
                    character=character,
                    place=place,
                    theme=theme,
                    story_text=story_data['story'],
                    story_history=[story_data]  # Initialize history with first story
                )
                
                # Redirect to story page
                return redirect('story_detail', session_id=session.session_id)
            
            except Exception as e:
                # Handle API errors gracefully
                error_message = f"Error generating story: {str(e)}"
                return render(request, 'story_app/home.html', {
                    'form': form,
                    'error': error_message
                })
    else:
        form = StoryInitiationForm()
    
    return render(request, 'story_app/home.html', {'form': form})


def story_detail(request, session_id):
    """
    Display the current story and choices.
    Shows a specific story session with options to continue.
    """
    # Get the story session
    session = get_object_or_404(StorySession, session_id=session_id)
    
    # Get the latest story part from history
    if session.story_history:
        latest_story = session.story_history[-1]
    else:
        latest_story = {'story': session.story_text, 'choice1': '', 'choice2': ''}
    
    context = {
        'session': session,
        'story': latest_story['story'],
        'moral': latest_story.get('moral', ''),
        'choice1': latest_story.get('choice1', ''),
        'choice2': latest_story.get('choice2', ''),
        'session_id': session_id,
    }
    
    return render(request, 'story_app/story.html', context)


@require_http_methods(["POST"])
def continue_story_view(request, session_id):
    """
    API endpoint to continue the story based on user choice.
    Receives AJAX POST request with selected choice.
    """
    try:
        # Get the story session
        session = get_object_or_404(StorySession, session_id=session_id)
        
        # Parse JSON request data
        data = json.loads(request.body)
        choice = data.get('choice', '')
        
        if not choice:
            return JsonResponse({'error': 'No choice selected'}, status=400)
        
        # Generate next story part
        next_story = continue_story(
            character=session.character,
            place=session.place,
            theme=session.theme,
            previous_story=session.story_history,
            user_choice=choice
        )
        
        # Add to history
        session.story_history.append(next_story)
        session.story_text = next_story['story']
        session.save()
        
        # Return the new story and choices
        return JsonResponse({
            'success': True,
            'story': next_story['story'],
            'moral': next_story.get('moral', ''),
            'choice1': next_story.get('choice1', ''),
            'choice2': next_story.get('choice2', ''),
        })
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({
            'error': f'Error generating story: {str(e)}'
        }, status=500)


def new_story(request):
    """
    Start a new story - redirect to home page.
    """
    return redirect('home')


def all_stories(request):
    """
    Display all saved story sessions (for admin/review).
    """
    stories = StorySession.objects.all()
    
    context = {
        'stories': stories,
    }
    
    return render(request, 'story_app/all_stories.html', context)
