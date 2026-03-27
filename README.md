# 🎭 AI Malayalam Kids Story Creator

A magical interactive web application that generates short Malayalam stories for kids (ages 3-6) with branching storytelling choices using AI.

## 🎯 Features

✨ **Story Generation**: Create unique Malayalam stories based on character, place, and theme  
🎨 **Interactive Choices**: Kids can make choices to direct the story  
💭 **Story Continuity**: AI maintains context for coherent story progression  
🌈 **Kid-Friendly UI**: Colorful, emoji-rich, large buttons, and simple layout  
📚 **Story Storage**: Save all generated stories for later viewing  
🧠 **Multiple AI Providers**: Support for both OpenAI and Google Gemini APIs  
🎯 **Simple Malayalam**: Age-appropriate vocabulary and sentences  

## 📋 Requirements

- Python 3.9+
- Django 4.2+
- OpenAI API Key OR Google Gemini API Key
- SQLite (included with Django)

## 🚀 Quick Start

### 1. Clone/Download the Project

```bash
cd C:\Users\think\OneDrive\Desktop\Projects\kunjukadha-ai\malayalam_story_creator
```

### 2. Create Virtual Environment

```powershell
# Using Python venv
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```powershell
# Copy the example file
Copy-Item .env.example .env

# Edit .env and add your API keys
notepad .env
```

**Choose one API provider:**

**Option A: Using Google Gemini (Recommended - Free)**
1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key to `.env` file:
```
AI_API_PROVIDER=gemini
GEMINI_API_KEY=your-api-key-here
```

**Option B: Using OpenAI**
1. Go to: https://platform.openai.com/api-keys
2. Create a new API key (requires paid account)
3. Copy the key to `.env` file:
```
AI_API_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
```

### 5. Initialize Database

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional - for Admin Panel)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://localhost:8000**

## 📖 Usage

### Creating a Story

1. Go to the homepage
2. Enter:
   - **Character** (Malayalam name): കുറുങ്ങന്‍, മാന്‍തി, കാക്ക, തുമ്പി, etc.
   - **Place** (Malayalam name): വനം, നദി, പാടി, കടൽ, പർവതം, etc.
   - **Theme**: Friendship, Kindness, Adventure, Learning, Courage, Family, Nature, Fun
3. Click "Create My Story"
4. Read the generated story and select a choice to continue

### Viewing All Stories

Visit `/all-stories/` to see all previously created stories

## 📁 Project Structure

```
malayalam_story_creator/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
│
├── malayalam_story_creator/
│   ├── __init__.py
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py
│
└── story_app/
    ├── migrations/
    ├── static/
    │   ├── css/
    │   │   └── style.css     # Main stylesheet
    │   └── js/
    │       └── main.js       # JavaScript
    │
    ├── templates/
    │   └── story_app/
    │       ├── home.html     # Home page
    │       ├── story.html    # Story display
    │       └── all_stories.html
    │
    ├── __init__.py
    ├── admin.py              # Admin configuration
    ├── apps.py               # App configuration
    ├── forms.py              # Django forms
    ├── models.py             # Database models
    ├── urls.py               # App URLs
    ├── utils.py              # AI integration
    └── views.py              # View logic
```

## 🔧 API Reference

### Main Views

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET, POST | Home page - create new story |
| `/story/<session_id>/` | GET | Display current story |
| `/api/story/<session_id>/continue/` | POST | Continue story (AJAX) |
| `/all-stories/` | GET | View all stories |
| `/new/` | GET | Start new story |

### POST `/api/story/<session_id>/continue/`

Request body:
```json
{
  "choice": "The selected choice text"
}
```

Response:
```json
{
  "success": true,
  "story": "Next part of the story...",
  "moral": "Moral lesson...",
  "choice1": "First choice...",
  "choice2": "Second choice..."
}
```

## 🧠 AI Prompt Design

The application uses carefully designed prompts to ensure:

1. **Simple Malayalam**: Age-appropriate vocabulary (3-6 years)
2. **Story Format**: 5-6 lines per story part
3. **Moral Lessons**: Each story includes a simple moral
4. **Interactive Choices**: 2 choices for story continuation
5. **Context Awareness**: Previous story parts are included for continuity
6. **Engaging Emojis**: Enhanced with emojis for visual appeal

## 🎨 Customization

### Changing Themes

Edit `story_app/forms.py` to add more themes:

```python
THEME_CHOICES = [
    ('your_theme', '🎨 Your Theme'),
    # Add more...
]
```

### Modifying Styles

Edit `story_app/static/css/style.css` to customize colors, fonts, and layouts

### Adjusting AI Prompts

Edit `story_app/utils.py` functions:
- `generate_initial_story()` - Initial story generation
- `continue_story()` - Story continuation

## 🐛 Troubleshooting

### API Key Issues

```
Error: "OPENAI_API_KEY not configured in environment"
```
- Make sure `.env` file exists and has the correct API key
- Restart the Django server after modifying `.env`

### Database Errors

```bash
# Reset database (WARNING: This deletes all data)
python manage.py flush
python manage.py migrate
```

### Import Errors

```bash
# Reinstall packages
pip install --upgrade -r requirements.txt
```

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones (iOS and Android)

## 🔒 Security Notes

For production deployment:

1. Change `DEBUG = False` in `malayalam_story_creator/settings.py`
2. Generate a new Django secret key
3. Add domain to `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Set up HTTPS
6. Use a production database (PostgreSQL/MySQL)

## 📦 Deployment

### Using Gunicorn + Nginx

```bash
# Install gunicorn (already in requirements.txt)
gunicorn malayalam_story_creator.wsgi:application
```

### Using Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "malayalam_story_creator.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as an AI Malayalam Kids Story Creator - Built with ❤️ for Kids

## 🙏 Acknowledgments

- Django framework
- OpenAI & Google Gemini APIs
- Malayalam language community
- All kids who inspire creativity!

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Django documentation: https://docs.djangoproject.com/
3. Check API documentation:
   - OpenAI: https://platform.openai.com/docs/
   - Gemini: https://ai.google.dev/docs

---

**🎭 Happy Story Creating! 🌟**
