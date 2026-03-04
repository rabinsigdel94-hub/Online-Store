# Quick Start Guide

## ✅ Your E-Commerce Store is Running!

**Server URL:** http://127.0.0.1:8000

## Login Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`

## What's Available

### Customer Features
1. **Browse Products** - http://127.0.0.1:8000/products/
2. **Search** - Use the search bar in navigation
3. **Shopping Cart** - Add products and checkout
4. **User Registration** - Create new customer accounts
5. **Product Reviews** - Rate and review products
6. **Order Tracking** - View order history and status

### Admin Features
1. **Admin Panel** - http://127.0.0.1:8000/admin/
   - Manage products, categories, orders
   - View customer information
   - Process orders and payments

## Sample Data Included

- 5 Categories (Electronics, Clothing, Books, Home & Kitchen, Sports)
- 8 Products with prices and stock
- Admin user ready to use

## How to Use

### As a Customer:
1. Visit http://127.0.0.1:8000
2. Register a new account or login
3. Browse products by category
4. Add items to cart
5. Proceed to checkout
6. Complete mock payment
7. View order confirmation

### As an Admin:
1. Login at http://127.0.0.1:8000/admin/
2. Add/edit products and categories
3. Manage orders and customers
4. View sales and inventory

## Mock Payment System

The payment system simulates real transactions:
- Credit Card (Mock)
- Debit Card (Mock)
- PayPal (Mock)

No real charges are made - perfect for testing!

## Stop the Server

Press `CTRL+C` in the terminal or close the terminal window.

## Restart the Server

Run: `run_server.bat`

Or manually:
```bash
venv\Scripts\activate
python manage.py runserver
```

## Project Structure

- `accounts/` - User authentication & profiles
- `products/` - Product catalog
- `cart/` - Shopping cart
- `orders/` - Order management
- `payments/` - Payment processing
- `reviews/` - Product reviews
- `templates/` - HTML templates
- `static/` - CSS/JS files
- `media/` - Uploaded images

## Next Steps

1. Add product images via admin panel
2. Create more categories and products
3. Test the complete checkout flow
4. Customize templates and styling
5. Add more features as needed

Enjoy your e-commerce platform! 🚀
