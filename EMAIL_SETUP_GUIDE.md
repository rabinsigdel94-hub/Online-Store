# Email Notification Setup Guide

## 📧 What's Been Added

Your e-commerce store now sends email notifications for orders!

### Email Notifications Sent:

1. **Customer Order Confirmation**
   - Sent to: Customer's email
   - When: After successful payment
   - Contains:
     - Order number and date
     - Items ordered with quantities and prices
     - Total amount
     - Shipping address
     - Link to view order details

2. **Admin Order Notification**
   - Sent to: Admin email
   - When: After successful payment
   - Contains:
     - Order number
     - Customer details
     - Items ordered
     - Shipping address
     - Link to admin panel

## 🔧 Current Setup (Development)

**Email Backend:** Console (emails print to terminal)

When you complete an order, you'll see the email content in your terminal/console where the Django server is running.

### How to Test:

1. Start the server: `python manage.py runserver`
2. Complete a purchase
3. Check the terminal - you'll see the email content printed there!

## 📮 Production Setup (Real Emails)

To send real emails in production, you need to configure SMTP settings.

### Option 1: Gmail SMTP (Easiest)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Create App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Name it "E-Store"
   - Copy the 16-character password

3. **Update `.env` file:**
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-16-char-app-password
   ADMIN_EMAIL=admin@yourdomain.com
   ```

4. **Update `ecommerce/settings.py`:**
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
   DEFAULT_FROM_EMAIL = f'E-Store <{EMAIL_HOST_USER}>'
   ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@estore.com')
   ```

### Option 2: SendGrid (Recommended for Production)

1. **Sign up:** https://sendgrid.com (Free tier: 100 emails/day)
2. **Create API Key**
3. **Update `.env`:**
   ```
   SENDGRID_API_KEY=your-api-key
   ADMIN_EMAIL=admin@yourdomain.com
   ```

4. **Install SendGrid:**
   ```bash
   pip install sendgrid
   ```

5. **Update settings:**
   ```python
   EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
   SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
   DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
   ```

### Option 3: AWS SES (Best for Scale)

1. **Sign up for AWS SES**
2. **Verify your domain**
3. **Get SMTP credentials**
4. **Update settings:**
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = os.getenv('AWS_SES_USER')
   EMAIL_HOST_PASSWORD = os.getenv('AWS_SES_PASSWORD')
   ```

## 📝 Email Templates

### Customer Email Template
Location: `templates/emails/order_confirmation.html`

Features:
- Beautiful HTML design
- Gradient header
- Order details table
- Shipping information
- "View Order" button
- Professional footer

### Customization:

**Change Colors:**
```css
.header { background: linear-gradient(135deg, #YOUR_COLOR1, #YOUR_COLOR2); }
```

**Change Logo:**
Add your logo in the header:
```html
<img src="YOUR_LOGO_URL" alt="E-Store" style="max-width: 200px;">
```

**Change Content:**
Edit `templates/emails/order_confirmation.html`

## 🧪 Testing Emails

### Test in Development (Console):

1. Complete an order
2. Check terminal output
3. You'll see:
   ```
   Subject: Order Confirmation - Order #123
   From: noreply@estore.com
   To: customer@email.com
   
   [Email content here]
   ```

### Test with Real Email:

1. Configure SMTP settings (see above)
2. Update `EMAIL_BACKEND` in settings
3. Complete a test order
4. Check your inbox!

## 📊 Email Content

### Customer Email Includes:

- ✅ Personalized greeting
- ✅ Order number and date
- ✅ Order status
- ✅ List of items with prices
- ✅ Total amount
- ✅ Shipping address
- ✅ Link to view order online
- ✅ Professional branding

### Admin Email Includes:

- ✅ New order alert
- ✅ Customer information
- ✅ Order details
- ✅ Items ordered
- ✅ Shipping address
- ✅ Direct link to admin panel

## 🔒 Security Best Practices

1. **Never commit email credentials** to Git
2. **Use environment variables** for sensitive data
3. **Use App Passwords** instead of real passwords
4. **Enable 2FA** on email accounts
5. **Use HTTPS** in production
6. **Verify sender domain** (SPF, DKIM records)

## 🎯 Email Triggers

Emails are sent when:
- ✅ Order is successfully paid
- ✅ Payment status changes to 'completed'
- ✅ Order status changes to 'processing'

Future triggers (to implement):
- Order shipped
- Order delivered
- Order cancelled
- Password reset
- Welcome email
- Abandoned cart reminder

## 📈 Email Analytics (Future)

Consider adding:
- Open rate tracking
- Click tracking
- Delivery status
- Bounce handling
- Unsubscribe management

## 🛠️ Troubleshooting

### Emails not sending?

1. **Check EMAIL_BACKEND:**
   - Console: Prints to terminal
   - SMTP: Sends real emails

2. **Check credentials:**
   - Verify EMAIL_HOST_USER
   - Verify EMAIL_HOST_PASSWORD
   - Check .env file

3. **Check Gmail settings:**
   - 2FA enabled?
   - App password created?
   - "Less secure apps" disabled?

4. **Check firewall:**
   - Port 587 open?
   - SMTP not blocked?

5. **Check logs:**
   - Look for error messages
   - Check Django console output

### Gmail blocking emails?

- Use App Password (not regular password)
- Enable 2-Factor Authentication
- Check "Less secure app access" (should be OFF)
- Use OAuth2 instead

### Emails going to spam?

- Set up SPF records
- Set up DKIM records
- Use verified domain
- Avoid spam trigger words
- Include unsubscribe link

## 📧 Email Best Practices

1. **Subject Lines:**
   - Clear and descriptive
   - Include order number
   - Keep under 50 characters

2. **Content:**
   - Personalize with customer name
   - Include all relevant details
   - Clear call-to-action
   - Mobile-responsive design

3. **Timing:**
   - Send immediately after order
   - Send updates promptly
   - Don't spam customers

4. **Design:**
   - Professional branding
   - Clean layout
   - Readable fonts
   - Proper spacing

## 🚀 Quick Start

**For Development (Console):**
- Already configured!
- Just complete an order
- Check terminal for email

**For Production (Gmail):**
1. Get Gmail App Password
2. Update .env file
3. Change EMAIL_BACKEND in settings
4. Test with real order

**For Production (SendGrid):**
1. Sign up for SendGrid
2. Get API key
3. Install sendgrid package
4. Update settings
5. Test emails

## 📝 Summary

Your store now sends:
- ✅ Beautiful HTML emails to customers
- ✅ Order notifications to admin
- ✅ Complete order details
- ✅ Professional branding
- ✅ Mobile-responsive design

Emails are currently set to **console mode** for development. Configure SMTP for production!
