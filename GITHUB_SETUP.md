# Push to GitHub Instructions

## Prerequisites

You need to install Git first:
1. Download Git from: https://git-scm.com/download/win
2. Install with default settings
3. Restart your terminal/command prompt

## Option 1: Using the Batch Script (Easiest)

1. Make sure Git is installed
2. Double-click `push_to_github.bat`
3. Enter your GitHub credentials when prompted

## Option 2: Manual Commands

Open Command Prompt or PowerShell in this directory and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Django E-Commerce Platform"

# Add remote repository
git remote add origin https://github.com/rabinsigdel94-hub/Online-Store.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## If Repository Already Exists

If you get an error that the repository already has content:

```bash
# Force push (WARNING: This will overwrite remote repository)
git push -u origin main --force
```

Or pull first then push:

```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

## Authentication

GitHub may ask for authentication:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your password)

### Creating a Personal Access Token:
1. Go to GitHub.com → Settings → Developer settings
2. Click "Personal access tokens" → "Tokens (classic)"
3. Click "Generate new token"
4. Select scopes: `repo` (full control)
5. Copy the token and use it as your password

## What Gets Pushed

All project files including:
- Django application code
- Templates and static files
- Configuration files
- Documentation (README, QUICKSTART, etc.)

**Note**: The following are excluded (via .gitignore):
- Virtual environment (venv/)
- Database file (db.sqlite3)
- Media uploads
- Python cache files
- .env file (secrets)

## After Pushing

Your repository will be available at:
https://github.com/rabinsigdel94-hub/Online-Store

## Troubleshooting

### "Git is not recognized"
- Install Git from https://git-scm.com/download/win
- Restart your terminal

### "Permission denied"
- Make sure you're logged into GitHub
- Use a Personal Access Token instead of password

### "Repository not found"
- Check the repository URL is correct
- Make sure the repository exists on GitHub
- Verify you have access to the repository

### "Failed to push"
- Check your internet connection
- Verify GitHub credentials
- Try: `git push -u origin main --force` (if you're sure)

## Future Updates

After making changes, push updates with:

```bash
git add .
git commit -m "Description of changes"
git push
```
