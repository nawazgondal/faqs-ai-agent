@echo off
REM FAQS AI Agent - Windows Batch Start Script
REM This script starts all services in separate terminals

echo.
echo ====================================
echo  FAQS AI Agent - System Startup
echo ====================================
echo.

REM Check if Ollama is running
tasklist | find /I "ollama" >nul
if errorlevel 1 (
    echo WARNING: Ollama is not running!
    echo Please start Ollama first: ollama serve
    echo.
    pause
) else (
    echo ✓ Ollama is running
)

REM Start Backend
echo.
echo Starting Backend (FastAPI)...
start cmd /k "cd backend && python main.py"
timeout /t 2 /nobreak

REM Start Frontend
echo.
echo Starting Frontend (Angular)...
start cmd /k "cd frontend && npm start"
timeout /t 2 /nobreak

echo.
echo ====================================
echo Services Starting:
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:4200
echo.
echo Docs:     http://localhost:8000/docs
echo.
echo Press any key to continue...
echo ====================================
pause
