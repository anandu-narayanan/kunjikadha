# ⚡ Quick Start Guide (5 Minutes)

Get the AI Malayalam Kids Story Creator running in 5 minutes!

## 🚀 The Fastest Way

### Step 1: Get API Key (2 min)
1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key

### Step 2: Create .env File (1 min)
Create a file named `.env` in the project folder with:
```
AI_API_PROVIDER=gemini
GEMINI_API_KEY=your-api-key-here
```

### Step 3: Run Setup
Double-click `run_server.bat` file in the project folder

OR in PowerShell:
```powershell
# Navigate to project
cd "C:\Users\think\OneDrive\Desktop\Projects\kunjukadha-ai\malayalam_story_creator"

# Activate environment
venv\Scripts\activate

# Start server
python manage.py runserver
```

### Step 4: Open Browser
Go to: http://localhost:8000

**That's it! 🎉**

---

## 📖 Quick Usage

1. **Home Page**
   - Enter character name (Malayalam, e.g., കാക്ക)
   - Enter place name (Malayalam, e.g., വനം)
   - Select theme
   - Click "Create My Story"

2. **Story Page**
   - Read the story
   - Select one of two choices
   - Story continues automatically! 

3. **Create Another Story**
   - Click "New Story"
   - Repeat from step 1

---

## 🆘 If Something Goes Wrong

**Error: "Python not found"**
- Install Python from https://www.python.org/downloads/
- Check "Add Python to PATH"

**Error: "Port 8000 already in use"**
```powershell
python manage.py runserver 8001
# Then go to: http://localhost:8001
```

**Error: "API Key error"**
- Make sure .env file is in the project root folder
- Double-check your API key is correct
- Don't include extra spaces or quotes around the key

**Error: "Module not found"**
```powershell
pip install -r requirements.txt
```

---

## 📚 Documentation

- **Full Setup Guide**: `SETUP_INSTRUCTIONS.md`
- **All Features**: `FEATURES.md`
- **API Documentation**: `API_DOCUMENTATION.md`
- **Docker Setup**: `DOCKER.md`

---

## ✨ Next Steps

- Customize themes in `story_app/forms.py`
- Change colors in `story_app/static/css/style.css`
- Explore admin panel at `/admin/`
- Create more stories!

---

**Made with ❤️ for Kids** 🎭✨

---

## Pro Tips

💡 **Tip 1**: Use Malayalam Unicode for characters and places
- Example: കാക്ക (crow), വനം (forest), നദി (river)

💡 **Tip 2**: The longer you continue a story, the more context it has
- Try making 5+ choices to see how the AI develops the narrative

💡 **Tip 3**: View all stories at `/all-stories/`
- Relive your favorite stories
- See story branching paths

💡 **Tip 4**: Admin panel at `/admin/` shows all stories
- Username/Password: Same as superuser

💡 **Tip 5**: Use Gemini API (Free) instead of OpenAI (Paid)
- Same quality stories, no cost!

---

**Need more help?** Check the README.md file for comprehensive documentation.
