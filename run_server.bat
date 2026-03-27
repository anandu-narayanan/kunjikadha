@echo off
REM AI Malayalam Kids Story Creator - Quick Start Script for Windows

echo.
echo ========================================
echo  AI Malayalam Kids Story Creator
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update packages (optional - comment out if not needed)
echo Installing packages...
pip install -q -r requirements.txt

REM Run migrations
echo Running migrations...
python manage.py migrate

REM Clear old static files and collect new ones
echo Collecting static files...
python manage.py collectstatic --noinput

REM Start server
echo.
echo ========================================
echo  Server is starting...
echo  Open your browser: http://localhost:8000
echo  Press Ctrl+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause
