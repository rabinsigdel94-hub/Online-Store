# Django E-Commerce Platform

A full-featured online store built with Django, featuring Amazon-like functionality.

## 🌟 Live Demo

**GitHub Repository**: https://github.com/rabinsigdel94-hub/Online-Store

## ✨ Features

- 🔐 User authentication & profiles with avatars
- 📦 Product catalog with categories & search
- 🛒 Shopping cart with session management
- 📋 Order management & tracking
- 💳 Mock payment system (Credit Card, Debit Card, PayPal)
- ⭐ Product reviews & ratings (1-5 stars)
- 👤 User profiles with order history
- 🎨 Professional Amazon-inspired UI design
- 📱 Responsive Bootstrap layout
- 🔍 Advanced search & filtering
- 🏪 Seller accounts support

## 🚀 Quick Setup

1. **Install Python 3.8+** from [python.org](https://www.python.org/downloads/)

2. **Clone the repository**:
   ```bash
   git clone https://github.com/rabinsigdel94-hub/Online-Store.git
   cd Online-Store
   ```

3. **Create virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Mac/Linux
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create sample data**:
   ```bash
   python create_sample_data.py
   ```

7. **Start the server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Website: http://127.0.0.1:8000
   - Admin Panel: http://127.0.0.1:8000/admin
   - Login: `admin` / `admin123`

## 📸 Screenshots

### Home Page
Professional Amazon-inspired design with featured categories and products.

### Product Catalog
Browse products with beautiful gradient placeholders and star ratings.

### Shopping Cart
Clean, intuitive cart interface with easy checkout process.

### Payment System
Mock payment system supporting multiple payment methods.

## 🛠️ Technology Stack

- **Backend**: Django 6.0.3
- **Frontend**: Bootstrap 5.3, FontAwesome 6.4
- **Database**: SQLite (development)
- **Authentication**: Django Auth System
- **Session Management**: Django Sessions

## 📁 Project Structure

- `accounts/` - User authentication & profiles
- `products/` - Product catalog & management
- `cart/` - Shopping cart functionality
- `orders/` - Order processing
- `payments/` - Payment integration
- `reviews/` - Product reviews & ratings


## 🎨 Design Features

- **Amazon-inspired color scheme**: Orange/yellow accents with dark navy navigation
- **Gradient backgrounds**: Beautiful gradient placeholders for products
- **Icon-based product images**: FontAwesome icons as professional placeholders
- **Smooth animations**: Card hover effects and transitions
- **Responsive layout**: Works perfectly on desktop, tablet, and mobile

## 🔒 Security Features

- CSRF protection on all forms
- Password hashing with Django's built-in system
- Session-based authentication
- SQL injection protection via Django ORM

## 📝 Sample Data Included

- 5 Categories (Electronics, Clothing, Books, Home & Kitchen, Sports)
- 8 Sample Products with prices and stock
- Admin user ready to use (admin/admin123)

## 🚀 Deployment

For production deployment:
1. Set `DEBUG=False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Configure HTTPS
6. Set strong `SECRET_KEY`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Rabin Sigdel**
- GitHub: [@rabinsigdel94-hub](https://github.com/rabinsigdel94-hub)

## 🙏 Acknowledgments

- Django framework for the robust backend
- Bootstrap for the responsive UI
- FontAwesome for the beautiful icons
- Amazon for design inspiration

---

**Note**: This is a demonstration project with a mock payment system. No real transactions are processed.
