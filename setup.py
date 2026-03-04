#!/usr/bin/env python
"""
Setup script for Django E-Commerce Platform
Run this after installing Python and creating virtual environment
"""
import os
import sys

def main():
    print("Django E-Commerce Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)
    
    print("✓ Python version OK")
    
    # Install requirements
    print("\nInstalling dependencies...")
    os.system("pip install -r requirements.txt")
    
    # Create .env file
    if not os.path.exists('.env'):
        print("\nCreating .env file...")
        os.system("copy .env.example .env" if os.name == 'nt' else "cp .env.example .env")
    
    # Create directories
    print("\nCreating directories...")
    os.makedirs('media', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Run migrations
    print("\nRunning migrations...")
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")
    
    # Create superuser prompt
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("\nNext steps:")
    print("1. Create superuser: python manage.py createsuperuser")
    print("2. Run server: python manage.py runserver")
    print("3. Visit: http://127.0.0.1:8000")
    print("4. Admin panel: http://127.0.0.1:8000/admin")

if __name__ == '__main__':
    main()
