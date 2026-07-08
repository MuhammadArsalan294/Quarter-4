@echo off
echo Starting Docker containers...
docker compose up -d --build
echo.
echo Containers started!
echo Frontend: http://localhost:3000
echo Backend: http://localhost:8000
echo.
echo After making code changes, run: docker compose restart
