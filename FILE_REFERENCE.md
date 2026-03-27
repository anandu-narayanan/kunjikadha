# 📑 Project File Reference

## 📍 Project Structure Overview

```
malayalam_story_creator/
│
├── 📄 Core Files
│   ├── manage.py                    # Django management script
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Example environment variables
│   ├── .gitignore                   # Git ignore rules
│   ├── run_server.bat               # Windows quick start script
│   └── Dockerfile                   # Docker configuration
│
├── 📚 Documentation
│   ├── README.md                    # Complete documentation
│   ├── QUICK_START.md               # 5-minute quick start
│   ├── SETUP_INSTRUCTIONS.md        # Detailed setup guide
│   ├── FEATURES.md                  # Complete features guide
│   ├── API_DOCUMENTATION.md         # API reference
│   ├── DOCKER.md                    # Docker setup guide
│   └── FILE_REFERENCE.md            # This file
│
├── 🏗️ Project Configuration
│   └── malayalam_story_creator/
│       ├── __init__.py              # Package marker
│       ├── settings.py              # Django settings (KEY FILE)
│       ├── urls.py                  # URL routing
│       └── wsgi.py                  # WSGI application
│
├── 🎨 Django Application
│   └── story_app/
│       ├── 📋 Python Files
│       │   ├── __init__.py          # App package marker
│       │   ├── admin.py             # Admin configuration
│       │   ├── apps.py              # App configuration
│       │   ├── models.py            # Database models (KEY FILE)
│       │   ├── views.py             # View logic (KEY FILE)
│       │   ├── urls.py              # App URLs
│       │   ├── forms.py             # Django forms (KEY FILE)
│       │   └── utils.py             # AI integration (KEY FILE)
│       │
│       ├── 🎨 Templates
│       │   └── story_app/
│       │       ├── home.html        # Home page (CHARACTER)
│       │       ├── story.html       # Story display (CHARACTER)
│       │       └── all_stories.html # Stories listing
│       │
│       └── 📦 Static Files
│           ├── css/
│           │   └── style.css        # Main stylesheet (CHARACTER)
│           └── js/
│               └── main.js          # JavaScript utilities
│
└── 📁 Generated Files (Auto-created)
    ├── db.sqlite3                   # Database
    ├── staticfiles/                 # Collected static files
    └── migrations/                  # Database migrations
```

---

## 🔑 Key Files Explained

### Configuration Files

#### `malayalam_story_creator/settings.py`
**Purpose**: Django configuration  
**Contains**:
- Installed apps
- Database configuration
- Static files settings
- API provider settings
```python
AI_API_PROVIDER = 'gemini'  # Choose AI provider
OPENAI_API_KEY = 'xxx'      # API keys from .env
GEMINI_API_KEY = 'xxx'
```

#### `.env`
**Purpose**: Store sensitive information  
**IMPORTANT**: Never commit to git!
```
AI_API_PROVIDER=gemini
GEMINI_API_KEY=your-key-here
DEBUG=True
```

#### `requirements.txt`
**Purpose**: Python dependencies  
**Key Packages**:
- Django 4.2.8
- openai 1.3.6
- google-generativeai 0.3.0
- python-dotenv 1.0.0

---

### Application Files

#### `story_app/models.py`
**Purpose**: Database schema  
**Model**: StorySession
```python
- session_id (UUID)      # Unique identifier
- character              # Malayalam character name
- place                  # Malayalam place name
- theme                  # Story theme
- story_text             # Current story content
- story_history          # All story parts (JSON)
- created_at, updated_at # Timestamps
```

#### `story_app/views.py`
**Purpose**: View logic and request handlers  
**Main Views**:
- `home()` - Display form and create stories
- `story_detail()` - Show current story
- `continue_story_view()` - AJAX endpoint for continuation
- `all_stories()` - List all stories

#### `story_app/utils.py`
**Purpose**: AI integration and story generation  
**Functions**:
- `generate_initial_story()` - Create initial story
- `continue_story()` - Generate next story part
- `call_ai_api()` - Route to correct API
- `parse_story_response()` - Extract story components

#### `story_app/forms.py`
**Purpose**: User input forms  
**Forms**:
- `StoryInitiationForm` - Character, place, theme
- `StoryChoiceForm` - Select story continuation

#### `story_app/urls.py`
**Purpose**: URL routing for the app  
**Routes**:
- `/` - Home
- `/story/<id>/` - Story display
- `/api/story/<id>/continue/` - AJAX endpoint
- `/all-stories/` - All stories listing
- `/new/` - New story

---

### Template Files

#### `story_app/templates/story_app/home.html`
**Purpose**: Home page with story creation form  
**Features**:
- Story form inputs
- Character/place suggestions
- Theme selection
- Feature showcase cards

#### `story_app/templates/story_app/story.html`
**Purpose**: Display current story and choices  
**Features**:
- Story text display
- Moral lesson section
- Interactive choice buttons
- Loading indicator
- AJAX for continuation

#### `story_app/templates/story_app/all_stories.html`
**Purpose**: List all created stories  
**Features**:
- Story cards grid
- Story metadata display
- Quick access to stories
- Empty state handling

---

### Static Files

#### `story_app/static/css/style.css`
**Purpose**: All styling (2000+ lines)  
**Sections**:
- Global styles & CSS variables
- Page layouts
- Form styling
- Button styling & animations
- Story container styling
- Choice buttons styling
- Responsive design

**Color Scheme**:
```css
--primary-color: #FF6B6B      (Red)
--secondary-color: #4ECDC4    (Teal)
--accent-color: #FFE66D       (Yellow)
```

#### `story_app/static/js/main.js`
**Purpose**: Client-side interactions  
**Features**:
- Form validation
- Click feedback
- Console messages
- Basic DOM manipulation

---

### Documentation Files

#### `README.md`
- Complete project overview
- Features list
- Installation instructions
- Usage guide
- Troubleshooting

#### `QUICK_START.md`
- 5-minute quick start
- Minimal setup
- Common issues

#### `SETUP_INSTRUCTIONS.md`
- Step-by-step Windows setup
- Virtual environment creation
- API key configuration
- Database initialization

#### `FEATURES.md`
- Detailed feature explanations
- Theme options
- Customization guide
- Malayalam word examples

#### `API_DOCUMENTATION.md`
- All API endpoints
- Request/response formats
- Example code
- Error codes
- Rate limiting info

#### `DOCKER.md`
- Docker setup
- Docker Compose usage
- Common Docker commands
- Troubleshooting

---

## 🔄 File Relationships

```
User Request
    ↓
urls.py (Route to view)
    ↓
views.py (Handle request)
    ↓
models.py (Database operations)
    ↓
utils.py (AI API calls)
    ↓
templates/ (Render HTML)
    ↓
static/ (Apply styling & interactions)
    ↓
Browser (Display to user)
```

---

## 📊 Dependencies Flow

```
settings.py (Configuration)
    ├── models.py (Database models)
    ├── views.py (Request handlers)
    ├── urls.py (URL routing)
    ├── forms.py (User input)
    └── utils.py (AI integration)

templates/ (HTML rendering)
    └── static/ (CSS & JS)

requirements.txt (Python packages)
    ├── Django
    ├── OpenAI/Gemini APIs
    └── Other utilities
```

---

## 🛠️ Editing Guide

### To Add a New Theme:
Edit: `story_app/forms.py`
```python
THEME_CHOICES = [
    ('new_theme', '🎨 New Theme'),
]
```

### To Change Colors:
Edit: `story_app/static/css/style.css`
```css
:root {
    --primary-color: #YOUR_COLOR;
}
```

### To Modify AI Prompts:
Edit: `story_app/utils.py`
- Search for `Generate a short interactive`
- Update prompt text

### To Add Database Field:
1. Edit: `story_app/models.py`
2. Run: `python manage.py makemigrations`
3. Run: `python manage.py migrate`

### To Add New View:
1. Add function to: `story_app/views.py`
2. Add URL to: `story_app/urls.py`
3. Create template if needed

---

## 📈 File Statistics

| Category | Files | Lines |
|----------|-------|-------|
| Python | 7 | ~800 |
| HTML | 3 | ~400 |
| CSS | 1 | ~2000 |
| JavaScript | 1 | ~50 |
| Documentation | 7 | ~2000 |
| Config | 6 | ~200 |
| **Total** | **25** | **~5500** |

---

## ✅ File Checklist

- [x] Core Django files (manage.py, settings, urls, wsgi)
- [x] App files (models, views, admin, forms, utils)
- [x] URL configuration (project & app)
- [x] Database models (StorySession)
- [x] Views & API endpoints
- [x] Forms (user input & choices)
- [x] AI integration (OpenAI & Gemini)
- [x] Responsive CSS styling (2000+ lines)
- [x] HTML templates (3 files)
- [x] JavaScript (forms & interactions)
- [x] Environment configuration (.env)
- [x] Requirements & dependencies
- [x] Docker support
- [x] Documentation (7 files)
- [x] Git ignore rules

---

## 🚀 Quick File Operations

```powershell
# Reset database (deletes all data)
python manage.py flush
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Create new migration
python manage.py makemigrations

# Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# View all URLs
python manage.py show_urls

# Run tests
python manage.py test
```

---

**Total Files Created**: 25+  
**Project Complete**: ✅  
**Ready to Run**: ✅  

---

For detailed information, see specific documentation files listed above.
