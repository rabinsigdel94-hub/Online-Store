# Test Email Notifications Now!

## 🎯 Quick Test Guide

Your store now sends email notifications! Here's how to test it right now:

### Step 1: Make Sure Server is Running

The server should be running at: http://127.0.0.1:8000

If not, start it:
```bash
python manage.py runserver
```

### Step 2: Complete a Test Order

1. **Go to the store:** http://127.0.0.1:8000
2. **Login** (or register if you haven't)
3. **Add items to cart:**
   - Browse products
   - Click "Add to Cart" on any product
4. **Go to cart:** Click cart icon in navbar
5. **Proceed to Checkout**
6. **Add/Select shipping address**
7. **Continue to Payment**
8. **Select any payment method** (it's mock, so any option works)
9. **Click "Complete Payment"**

### Step 3: Check Your Terminal!

After completing the order, look at your terminal/console where Django is running.

You should see TWO emails printed:

#### Email 1: Customer Confirmation
```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order Confirmation - Order #1
From: E-Store <noreply@estore.com>
To: customer@email.com

Hi username,

Thank you for your order!

Order Details:
Order Number: #1
Total Amount: $XX.XX
...
```

#### Email 2: Admin Notification
```
Subject: New Order Received - Order #1
From: E-Store <noreply@estore.com>
To: admin@estore.com

New Order Received!

Order Details:
Order Number: #1
Customer: username (email@example.com)
...
```

### Step 4: View the Beautiful HTML Email

The customer receives a beautifully designed HTML email with:
- 🎨 Gradient header
- 📦 Order details
- 💰 Total amount
- 📍 Shipping address
- 🔗 Link to view order
- ✨ Professional design

## 📧 What Emails Contain

### Customer Email:
- Personalized greeting
- Order number and date
- List of items ordered
- Quantities and prices
- Total amount
- Shipping address
- Link to view order online
- Professional branding

### Admin Email:
- New order alert
- Customer name and email
- Order details
- Items ordered
- Shipping information
- Direct link to admin panel

## 🔧 Current Setup

**Mode:** Console (Development)
- Emails print to terminal
- No real emails sent
- Perfect for testing!

**To Send Real Emails:**
See EMAIL_SETUP_GUIDE.md for:
- Gmail SMTP setup
- SendGrid setup
- AWS SES setup

## 🎨 Email Design Features

The HTML email includes:
- Beautiful gradient header (purple/pink)
- Clean, professional layout
- Order details in a card
- Item list with prices
- Total amount highlighted
- Shipping address formatted nicely
- "View Order Details" button
- Professional footer
- Mobile-responsive design

## 💡 Tips

1. **Check Terminal:** Always look at the terminal where Django is running
2. **Scroll Up:** Emails might be above recent logs
3. **Multiple Orders:** Each order generates 2 emails (customer + admin)
4. **HTML Version:** The HTML email is much prettier than the plain text version

## 🚀 Next Steps

After testing in console mode:

1. **For Production:**
   - Set up Gmail SMTP (easiest)
   - Or use SendGrid (recommended)
   - Or use AWS SES (for scale)

2. **Customize Emails:**
   - Edit `templates/emails/order_confirmation.html`
   - Change colors, logo, text
   - Add your branding

3. **Add More Emails:**
   - Order shipped notification
   - Order delivered notification
   - Welcome email for new users
   - Password reset emails

## 📝 Example Terminal Output

When you complete an order, you'll see something like this in your terminal:

```
[05/Mar/2026 19:00:00] "POST /payments/process/1/ HTTP/1.1" 302 0

Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order Confirmation - Order #1
From: E-Store <noreply@estore.com>
To: john@example.com
Date: Wed, 05 Mar 2026 19:00:00 -0000
Message-ID: <...>

Hi john,

Thank you for your order!

Order Details:
Order Number: #1
Total Amount: $149.99
Status: Processing

Items:
- Nike Air Max 270 x 1 = $149.99

Shipping Address:
John Doe
123 Main Street
New York, NY 10001

We'll send you another email when your order ships.

Thank you for shopping with us!

E-Store Team

-------------------------------------------------------------------------------

Content-Type: text/plain; charset="utf-8"
Subject: New Order Received - Order #1
From: E-Store <noreply@estore.com>
To: admin@estore.com

New Order Received!

Order Details:
Order Number: #1
Customer: john (john@example.com)
Total Amount: $149.99
...
```

## ✅ Success Indicators

You know emails are working when:
- ✅ You see email content in terminal
- ✅ Two emails appear (customer + admin)
- ✅ Order details are correct
- ✅ No error messages
- ✅ Success message appears on website

## 🎉 Ready to Test!

Go ahead and complete a test order now. Watch your terminal for the email notifications!

**Quick Link:** http://127.0.0.1:8000

Happy testing! 📧
