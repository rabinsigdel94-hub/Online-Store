# Complete Purchase Flow with Email

## 📋 Step-by-Step Purchase Process

### Step 1: Add Items to Cart
- Browse products
- Click "Add to Cart"
- Items added to shopping cart

### Step 2: Go to Checkout
- Click cart icon
- Click "Proceed to Checkout"
- **YOU ARE HERE** → Checkout page with address form

### Step 3: Add/Select Shipping Address
**This is the page you're seeing in your screenshot:**
- Full name
- Phone
- Address line 1
- Address line 2
- City
- State
- Postal code
- Country
- Is default checkbox
- Click "Add Address" or "Continue to Payment"

**Note:** Email is NOT collected here because the customer already provided their email when they registered/logged in!

### Step 4: Payment Page
After clicking "Continue to Payment", customer sees:
- Order summary
- Payment method selection (Credit Card, Debit Card, PayPal)
- "Complete Payment" button

### Step 5: Complete Payment ✨
**When customer clicks "Complete Payment":**

```python
# This happens in payments/views.py:

1. Payment is processed
2. Order status updated to "paid"
3. ✉️ Email sent to CUSTOMER (order confirmation)
4. ✉️ Email sent to ADMIN (new order notification)
5. Success message shown
6. Redirect to "Payment Done" page
```

### Step 6: Confirmation
Customer sees:
- "Payment Successful!" message
- "Check your email for confirmation"
- Order details
- Link to view order

## 📧 Where Does Email Come From?

The customer's email is taken from their **user account**:

```python
# In payments/views.py:
send_mail(
    subject='Order Confirmation',
    message='...',
    from_email='noreply@estore.com',
    recipient_list=[order.user.email],  # ← Email from user account!
)
```

When a user registers, they provide:
- Username
- **Email** ← This is used for order confirmations!
- Password

## 🔍 Why No Email Field on Checkout?

Because:
1. User is already logged in
2. Their email is in their account
3. No need to ask again!
4. Prevents typos/errors
5. Better user experience

## 🧪 Test the Complete Flow:

1. **Login** at http://127.0.0.1:8000/accounts/login/
   - Your account has an email address

2. **Add items to cart**
   - Browse products
   - Click "Add to Cart"

3. **Go to checkout**
   - Fill in shipping address (the form you showed)
   - Click "Continue to Payment"

4. **Complete payment**
   - Select payment method
   - Click "Complete Payment"

5. **Check terminal!**
   - You'll see email sent to: `your-account-email@example.com`
   - Email contains order confirmation

## 📝 Example Email Output in Terminal:

```
Subject: Order Confirmation - Order #1
From: E-Store <noreply@estore.com>
To: john@example.com  ← Email from user's account!

Hi john,

Thank you for your order!

Order Details:
Order Number: #1
Total Amount: $149.99
...
```

## ✅ Summary

**Email is sent automatically when:**
- ✅ Customer completes payment
- ✅ Uses email from their account
- ✅ No need to enter email on checkout page
- ✅ Sent to both customer and admin

**To see the email:**
1. Complete the full purchase flow
2. Click "Complete Payment" on payment page
3. Check your terminal/console
4. Email will be there!

The email function IS working - it just happens at the END of the process, not on the address form! 🎉
