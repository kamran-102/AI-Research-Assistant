@echo off
title Biomedical Research Analyst Launcher

echo Starting Backend Server...
start cmd /k "cd backend && uvicorn main_fastapi:app --reload"

timeout /t 3 >nul

echo Starting Frontend...
start cmd /k "cd frontend && streamlit run streamlit_app.py"

echo.
echo ---------------------------------------
echo Backend:  http://127.0.0.1:8000
echo Frontend: http://localhost:8501
echo ---------------------------------------
echo.

pause