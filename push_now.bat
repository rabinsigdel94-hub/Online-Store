@echo off
echo ========================================
echo Pushing to GitHub
echo ========================================
echo.

REM Check if git is available
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git is not found in PATH
    echo.
    echo Please do ONE of the following:
    echo 1. Close this window and open a NEW Command Prompt
    echo 2. Or restart your computer
    echo 3. Or add Git to PATH manually
    echo.
    echo Then run this script again.
    pause
    exit /b 1
)

echo Git found! Proceeding...
echo.

REM Initialize repository
echo [1/7] Initializing git repository...
git init
if %ERRORLEVEL% NEQ 0 (
    echo Failed to initialize repository
    pause
    exit /b 1
)

REM Add all files
echo [2/7] Adding all files...
git add .
if %ERRORLEVEL% NEQ 0 (
    echo Failed to add files
    pause
    exit /b 1
)

REM Create commit
echo [3/7] Creating commit...
git commit -m "Initial commit: Django E-Commerce Platform with Amazon-like features"
if %ERRORLEVEL% NEQ 0 (
    echo Failed to create commit
    pause
    exit /b 1
)

REM Add remote
echo [4/7] Adding remote repository...
git remote add origin https://github.com/rabinsigdel94-hub/Online-Store.git 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Remote already exists, updating...
    git remote set-url origin https://github.com/rabinsigdel94-hub/Online-Store.git
)

REM Set branch name
echo [5/7] Setting branch to main...
git branch -M main

REM Push to GitHub
echo [6/7] Pushing to GitHub...
echo.
echo You will be prompted for credentials:
echo Username: rabinsigdel94-hub
echo Password: Use your Personal Access Token (NOT your GitHub password)
echo.
echo If you don't have a token, create one at:
echo https://github.com/settings/tokens
echo.
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo SUCCESS! Code pushed to GitHub!
    echo ========================================
    echo.
    echo Your repository is now live at:
    echo https://github.com/rabinsigdel94-hub/Online-Store
    echo.
) else (
    echo.
    echo ========================================
    echo Push failed!
    echo ========================================
    echo.
    echo Common issues:
    echo 1. Wrong credentials - Use Personal Access Token
    echo 2. Repository doesn't exist - Create it on GitHub first
    echo 3. Network issues - Check your internet connection
    echo.
    echo Need help? Check GITHUB_SETUP.md
    echo.
)

pause
