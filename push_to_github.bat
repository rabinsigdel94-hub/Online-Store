@echo off
echo ========================================
echo Pushing E-Commerce Project to GitHub
echo ========================================
echo.

REM Initialize git repository
git init

REM Add all files
git add .

REM Create initial commit
git commit -m "Initial commit: Django E-Commerce Platform with Amazon-like features"

REM Add remote repository
git remote add origin https://github.com/rabinsigdel94-hub/Online-Store.git

REM Push to GitHub
git branch -M main
git push -u origin main

echo.
echo ========================================
echo Done! Code pushed to GitHub
echo ========================================
pause
