# 🚀 Complete Setup Instructions for Windows

This guide will walk you through setting up the AI Malayalam Kids Story Creator on Windows.

## ✅ Prerequisites Check

Before starting, make sure you have:
- [ ] Windows 10 or later
- [ ] Internet connection
- [ ] About 500 MB free disk space

## Step 1️⃣: Install Python

1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 (latest stable)
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

**Verify Python installation:**
```powershell
python --version
```

You should see: `Python 3.x.x`

## Step 2️⃣: Navigate to Project Directory

Open PowerShell (Right-click → "Open PowerShell Here") in the project folder:
```
C:\Users\think\OneDrive\Desktop\Projects\kunjukadha-ai\malayalam_story_creator
```

Or use this command:
```powershell
Set-Location "C:\Users\think\OneDrive\Desktop\Projects\kunjukadha-ai\malayalam_story_creator"
```

## Step 3️⃣: Create Virtual Environment

A virtual environment keeps project dependencies isolated.

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

You should see `(venv)` at the beginning of the terminal line.

**If you see an error about execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activation again.

## Step 4️⃣: Install Python Packages

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

Wait for installation to complete (may take 2-3 minutes).

**Verify installation:**
```powershell
pip list
```

You should see Django and other packages listed.

## Step 5️⃣: Set Up Environment Variables

### Create .env File

```powershell
# Copy the example file
Copy-Item .env.example .env

# Open .env in Notepad
notepad .env
```

### Get API Key (Choose One)

**Option 1: Google Gemini (FREE - RECOMMENDED)**

1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the API key
4. In the .env file, paste:
```
AI_API_PROVIDER=gemini
GEMINI_API_KEY=your-api-key-here
```

**Option 2: OpenAI ($)**

1. Go to: https://platform.openai.com/api-keys
2. Create account and add payment method
3. Create API key
4. In the .env file, paste:
```
AI_API_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
```

5. Save the .env file (Ctrl+S, then close)

## Step 6️⃣: Initialize Database

```powershell
python manage.py migrate
```

You should see: "Operations to perform: ... OK"

## Step 7️⃣: Create Admin User (Optional)

This allows you to access `/admin/` panel:

```powershell
python manage.py createsuperuser
```

Follow the prompts:
- Username: admin
- Email: admin@example.com
- Password: (choose a strong password)

## Step 8️⃣: Run Development Server

```powershell
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Step 9️⃣: Open in Browser

1. Open your web browser
2. Go to: http://localhost:8000
3. Start creating stories! 🎉

## 🎮 Using the Application

### Create a Story
1. On home page, enter:
   - Character (Malayalam): കാക്ക, കുറുങ്ങന്‍, മാന്‍തി, എലിപ്പോ, etc.
   - Place (Malayalam): വനം, നദി, പാടി, കടൽ, etc.
   - Theme: Select from dropdown
2. Click "Create My Story"
3. Make choices to continue the story

### View Admin Panel
1. Go to: http://localhost:8000/admin
2. Login with superuser credentials
3. View all created stories

## 🆘 Troubleshooting

### Issue: "Python not found"
**Solution:**
- Restart PowerShell
- Check if Python is in PATH
- Reinstall Python and check "Add Python to PATH"

### Issue: Virtual environment won't activate
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activation again.

### Issue: "Port 8000 already in use"
**Solution:**
```powershell
python manage.py runserver 8001
# Then go to: http://localhost:8001
```

### Issue: "API Key error"
**Solution:**
- Verify .env file exists in project root
- Check API key is correct (copy-paste again from provider)
- Restart Django server (Ctrl+C, then run again)

### Issue: Database "No such table: story_app_storysession"
**Solution:**
```powershell
python manage.py migrate
```

## 📝 Important Files

| File | Purpose |
|------|---------|
| `manage.py` | Django management script |
| `.env` | Your API keys (keep secret!) |
| `requirements.txt` | Python dependencies |
| `db.sqlite3` | Database file (auto-created) |

## 🛑 Stopping the Server

In PowerShell: Press `Ctrl+C`

## 🔄 Restarting

```powershell
# Make sure you're in project directory
cd "C:\Users\think\OneDrive\Desktop\Projects\kunjukadha-ai\malayalam_story_creator"

# Activate environment
venv\Scripts\activate

# Start server
python manage.py runserver
```

## 📦 Deactivating Virtual Environment

When done for the day:
```powershell
deactivate
```

## 🌐 Accessing from Another Device

On the same network, use your computer's IP:
```
http://YOUR_IP_ADDRESS:8000
```

Find your IP:
```powershell
ipconfig
```

Look for "IPv4 Address" under your active connection.

## 🚀 Next Steps

- Customize themes in `story_app/forms.py`
- Modify styles in `story_app/static/css/style.css`
- Adjust AI prompts in `story_app/utils.py`
- Add more features as needed!

## 📚 Resources

- Django Documentation: https://docs.djangoproject.com/
- Gemini API Docs: https://ai.google.dev/
- OpenAI Docs: https://platform.openai.com/docs/

## ✨ You're All Set! 🎉

Congratulations! Your AI Malayalam Kids Story Creator is ready to use.

**Common Commands Reference:**

```powershell
# Activate environment
venv\Scripts\activate

# Deactivate environment
deactivate

# Start server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Open shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

**Made with ❤️ for Kids** 🎭✨
