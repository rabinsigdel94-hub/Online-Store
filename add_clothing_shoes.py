import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from accounts.models import User
from products.models import Category, Product
from django.utils.text import slugify

print("Adding Clothing and Shoes Collection...")
print("=" * 60)

# Get admin user
admin = User.objects.filter(username='admin').first()
if not admin:
    print("Error: Admin user not found. Please run create_sample_data.py first")
    exit(1)

# Get or create categories
clothing_cat, _ = Category.objects.get_or_create(
    slug='clothing',
    defaults={'name': 'Clothing', 'description': 'Fashion and apparel for everyone'}
)

shoes_cat, _ = Category.objects.get_or_create(
    slug='shoes',
    defaults={'name': 'Shoes', 'description': 'Branded footwear collection'}
)

# Clothing Products
clothing_products = [
    # Men's Clothing
    {'name': 'Nike Dri-FIT T-Shirt', 'price': 29.99, 'stock': 150, 'description': 'Premium athletic t-shirt with moisture-wicking technology'},
    {'name': 'Adidas Essentials Hoodie', 'price': 59.99, 'stock': 100, 'description': 'Comfortable cotton blend hoodie with kangaroo pocket'},
    {'name': 'Levi\'s 501 Original Jeans', 'price': 79.99, 'stock': 120, 'description': 'Classic straight fit jeans, original since 1873'},
    {'name': 'Ralph Lauren Polo Shirt', 'price': 89.99, 'stock': 80, 'description': 'Iconic polo shirt with signature embroidered pony'},
    {'name': 'Champion Sweatpants', 'price': 44.99, 'stock': 90, 'description': 'Soft fleece sweatpants with elastic waistband'},
    {'name': 'Tommy Hilfiger Jacket', 'price': 129.99, 'stock': 60, 'description': 'Water-resistant windbreaker with signature flag logo'},
    {'name': 'Under Armour Compression Shirt', 'price': 39.99, 'stock': 110, 'description': 'HeatGear fabric keeps you cool and dry'},
    {'name': 'Puma Track Jacket', 'price': 69.99, 'stock': 75, 'description': 'Retro-inspired track jacket with side stripe detail'},
    
    # Women's Clothing
    {'name': 'Zara Floral Dress', 'price': 49.99, 'stock': 85, 'description': 'Elegant floral print midi dress, perfect for any occasion'},
    {'name': 'H&M Skinny Jeans', 'price': 39.99, 'stock': 140, 'description': 'Stretch denim skinny jeans with high waist'},
    {'name': 'Forever 21 Crop Top', 'price': 19.99, 'stock': 200, 'description': 'Trendy crop top in various colors'},
    {'name': 'Gap Denim Jacket', 'price': 79.99, 'stock': 70, 'description': 'Classic denim jacket with button closure'},
    {'name': 'Uniqlo Cashmere Sweater', 'price': 99.99, 'stock': 55, 'description': 'Luxuriously soft 100% cashmere sweater'},
    {'name': 'Mango Leather Jacket', 'price': 199.99, 'stock': 40, 'description': 'Genuine leather biker jacket with zipper details'},
    {'name': 'Victoria\'s Secret Yoga Pants', 'price': 54.99, 'stock': 130, 'description': 'High-waisted yoga pants with pocket'},
    {'name': 'Calvin Klein Sports Bra', 'price': 34.99, 'stock': 160, 'description': 'Medium support sports bra with logo band'},
]

# Shoes Products
shoes_products = [
    # Athletic Shoes
    {'name': 'Nike Air Max 270', 'price': 149.99, 'stock': 80, 'description': 'Iconic Air Max cushioning with modern design'},
    {'name': 'Adidas Ultraboost 22', 'price': 189.99, 'stock': 65, 'description': 'Premium running shoes with Boost technology'},
    {'name': 'New Balance 574', 'price': 84.99, 'stock': 95, 'description': 'Classic lifestyle sneaker with ENCAP midsole'},
    {'name': 'Puma RS-X', 'price': 109.99, 'stock': 70, 'description': 'Bold retro-futuristic running shoes'},
    {'name': 'Reebok Classic Leather', 'price': 74.99, 'stock': 100, 'description': 'Timeless leather sneakers, comfortable and durable'},
    {'name': 'Under Armour HOVR Phantom', 'price': 139.99, 'stock': 60, 'description': 'Connected running shoes with UA HOVR cushioning'},
    
    # Casual Shoes
    {'name': 'Converse Chuck Taylor All Star', 'price': 59.99, 'stock': 150, 'description': 'Iconic canvas sneakers, a timeless classic'},
    {'name': 'Vans Old Skool', 'price': 64.99, 'stock': 120, 'description': 'Classic skate shoes with signature side stripe'},
    {'name': 'Skechers Go Walk', 'price': 69.99, 'stock': 90, 'description': 'Ultra-lightweight walking shoes with Goga Mat insole'},
    {'name': 'Crocs Classic Clogs', 'price': 49.99, 'stock': 200, 'description': 'Comfortable foam clogs, perfect for casual wear'},
    
    # Formal Shoes
    {'name': 'Clarks Desert Boots', 'price': 129.99, 'stock': 55, 'description': 'Premium suede desert boots with crepe sole'},
    {'name': 'Dr. Martens 1460', 'price': 169.99, 'stock': 45, 'description': 'Iconic 8-eye leather boots with air-cushioned sole'},
    {'name': 'Timberland 6-Inch Premium Boots', 'price': 189.99, 'stock': 50, 'description': 'Waterproof leather boots, built to last'},
    {'name': 'Cole Haan Oxford Shoes', 'price': 149.99, 'stock': 40, 'description': 'Classic leather oxford dress shoes'},
    
    # Women's Shoes
    {'name': 'Steve Madden Heels', 'price': 89.99, 'stock': 75, 'description': 'Stylish high heels for any occasion'},
    {'name': 'UGG Classic Mini Boots', 'price': 169.99, 'stock': 60, 'description': 'Cozy sheepskin boots with signature comfort'},
    {'name': 'Birkenstock Arizona Sandals', 'price': 99.99, 'stock': 110, 'description': 'Comfortable cork footbed sandals'},
    {'name': 'Sam Edelman Ballet Flats', 'price': 119.99, 'stock': 85, 'description': 'Elegant leather ballet flats'},
]

# Add clothing products
print("\nAdding Clothing Products:")
print("-" * 60)
for prod_data in clothing_products:
    prod, created = Product.objects.get_or_create(
        slug=slugify(prod_data['name']),
        defaults={
            'name': prod_data['name'],
            'category': clothing_cat,
            'seller': admin,
            'description': prod_data['description'],
            'price': prod_data['price'],
            'stock': prod_data['stock'],
            'available': True
        }
    )
    if created:
        print(f"✓ {prod_data['name']} - ${prod_data['price']}")

# Add shoes products
print("\nAdding Shoes Products:")
print("-" * 60)
for prod_data in shoes_products:
    prod, created = Product.objects.get_or_create(
        slug=slugify(prod_data['name']),
        defaults={
            'name': prod_data['name'],
            'category': shoes_cat,
            'seller': admin,
            'description': prod_data['description'],
            'price': prod_data['price'],
            'stock': prod_data['stock'],
            'available': True
        }
    )
    if created:
        print(f"✓ {prod_data['name']} - ${prod_data['price']}")

print("\n" + "=" * 60)
print("✓ Successfully added clothing and shoes collection!")
print(f"\nTotal Products Added:")
print(f"  - Clothing: {len(clothing_products)} items")
print(f"  - Shoes: {len(shoes_products)} items")
print(f"  - Total: {len(clothing_products) + len(shoes_products)} items")
print("\nYou can now:")
print("1. Visit http://127.0.0.1:8000 to see the new products")
print("2. Go to admin panel to add product images")
print("3. Browse by category: Clothing or Shoes")
print("=" * 60)
