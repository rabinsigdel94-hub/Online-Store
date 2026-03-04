import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from accounts.models import User
from products.models import Category, Product
from django.utils.text import slugify

print("Creating sample data...")

# Get or create admin user
admin = User.objects.filter(username='admin').first()
if not admin:
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✓ Admin user created")

# Create categories
categories_data = [
    {'name': 'Electronics', 'description': 'Latest electronic gadgets and devices'},
    {'name': 'Clothing', 'description': 'Fashion and apparel for everyone'},
    {'name': 'Books', 'description': 'Wide selection of books'},
    {'name': 'Home & Kitchen', 'description': 'Everything for your home'},
    {'name': 'Sports', 'description': 'Sports equipment and gear'},
]

categories = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        slug=slugify(cat_data['name']),
        defaults={
            'name': cat_data['name'],
            'description': cat_data['description']
        }
    )
    categories[cat_data['name']] = cat
    if created:
        print(f"✓ Created category: {cat_data['name']}")

# Create products
products_data = [
    {'name': 'Wireless Headphones', 'category': 'Electronics', 'price': 79.99, 'stock': 50},
    {'name': 'Smart Watch', 'category': 'Electronics', 'price': 199.99, 'stock': 30},
    {'name': 'Laptop Stand', 'category': 'Electronics', 'price': 29.99, 'stock': 100},
    {'name': 'Men T-Shirt', 'category': 'Clothing', 'price': 19.99, 'stock': 200},
    {'name': 'Women Jeans', 'category': 'Clothing', 'price': 49.99, 'stock': 150},
    {'name': 'Python Programming Book', 'category': 'Books', 'price': 39.99, 'stock': 75},
    {'name': 'Coffee Maker', 'category': 'Home & Kitchen', 'price': 89.99, 'stock': 40},
    {'name': 'Yoga Mat', 'category': 'Sports', 'price': 24.99, 'stock': 120},
]

for prod_data in products_data:
    prod, created = Product.objects.get_or_create(
        slug=slugify(prod_data['name']),
        defaults={
            'name': prod_data['name'],
            'category': categories[prod_data['category']],
            'seller': admin,
            'description': f"High quality {prod_data['name']} at an amazing price!",
            'price': prod_data['price'],
            'stock': prod_data['stock'],
            'available': True
        }
    )
    if created:
        print(f"✓ Created product: {prod_data['name']}")

print("\n✓ Sample data created successfully!")
print("\nYou can now:")
print("1. Run server: python manage.py runserver")
print("2. Visit: http://127.0.0.1:8000")
print("3. Admin login: username=admin, password=admin123")
