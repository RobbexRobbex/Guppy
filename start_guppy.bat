@echo off
echo Starting Flask backend...
start cmd /k python app.py

timeout /t 2 > nul

echo Starting web server for frontend...
start cmd /k python -m http.server 8000

echo Opening browser...
start http://localhost:8000/index.html
