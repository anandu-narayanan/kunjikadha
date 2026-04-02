# Kunjikkadha

Kunjikkadha is a Django web app that generates short interactive Malayalam stories for young children. A user chooses a character, a place, and a theme, and the app asks an AI model to create a simple story segment with two child-friendly choices for what happens next.

Each story session is saved in SQLite so the story can be reopened and continued later from the latest branch point.

## Features

- Generate short Malayalam children's stories from a simple prompt form
- Continue each story interactively through two follow-up choices
- Store story sessions and story history in SQLite
- Switch between OpenAI and Gemini through environment variables
- Browse previously generated stories from a saved stories page
- Kid-friendly UI with large cards, readable text, and simple navigation

## Tech Stack

- Python
- Django 4.2
- SQLite
- OpenAI API
- Google Gemini API
- HTML, CSS, and vanilla JavaScript

## How It Works

1. The home page collects a character, place, and theme.
2. The app sends a structured prompt to the configured AI provider.
3. The AI response is parsed into:
   - `story`
   - `moral`
   - `choice1`
   - `choice2`
4. A `StorySession` record is created and the first story part is stored in `story_history`.
5. When the reader selects a choice, the app sends the previous story context plus the selected choice back to the AI and saves the next story segment.

## Project Structure

```text
malayalam_story_creator/
|-- manage.py
|-- requirements.txt
|-- malayalam_story_creator/
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- story_app/
    |-- forms.py
    |-- models.py
    |-- urls.py
    |-- utils.py
    |-- views.py
    |-- migrations/
    |-- static/
    `-- templates/
```

## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Add a `.env` file in the project root:

```env
SECRET_KEY=django-insecure-change-me
DEBUG=True
AI_API_PROVIDER=gemini

# Use one or both depending on your provider choice
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

Notes:

- `AI_API_PROVIDER` accepts `gemini` or `openai`
- Only the API key for the provider you use is required
- The current settings file defaults to `gemini` when `AI_API_PROVIDER` is not set

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main Routes

- `/` - Story creation form
- `/story/<session_id>/` - Read the latest story part and choose what happens next
- `/api/story/<session_id>/continue/` - AJAX endpoint that generates the next story part
- `/all-stories/` - View saved stories
- `/admin/` - Django admin

## Core Components

### `story_app/views.py`

Handles:

- starting a new story session
- rendering the current story
- continuing the story from a selected choice
- listing saved story sessions

### `story_app/utils.py`

Contains the AI integration logic:

- builds prompts for initial and continued story generation
- calls the selected provider
- parses model output into structured story data

### `story_app/models.py`

Defines `StorySession`, which stores:

- `session_id`
- `character`
- `place`
- `theme`
- `story_text`
- `story_history`
- timestamps

## Environment and Configuration

Current project behavior from `settings.py`:

- uses SQLite by default
- loads environment variables from `.env`
- runs with `DEBUG = True`
- sets `AI_API_PROVIDER` to `gemini` by default if unset

This makes the app convenient for local development, but it should be hardened before production use.

## Notes

- Story history is stored in a JSON field so each generated segment can be reused as context.
- The app expects the AI response to follow a strict marker format: `STORY`, `MORAL`, `CHOICE1`, and `CHOICE2`.
- If the provider response format changes or the API call fails, the app will surface an error on the page or via JSON in the continue endpoint.

## Future Improvements

- add automated tests for views and prompt parsing
- support more theme presets and custom themes
- improve admin tools for reviewing generated stories
- add production settings for static files, secrets, and deployment
- improve response validation when the AI output does not match the expected format
