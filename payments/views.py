from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Payment
from orders.models import Order
import uuid

@login_required
def payment_process(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        transaction_id = f"MOCK-{uuid.uuid4().hex[:12].upper()}"
        
        payment = Payment.objects.create(
            order=order,
            payment_method=payment_method,
            transaction_id=transaction_id,
            amount=order.total_amount,
            status='completed'
        )
        
        order.payment_status = 'paid'
        order.status = 'processing'
        order.save()
        
        # Send email to customer
        send_order_confirmation_email(order)
        
        # Send email to admin
        send_admin_notification_email(order)
        
        messages.success(request, 'Payment successful! Check your email for confirmation.')
        return redirect('payments:done', order_id=order.id)
    
    return render(request, 'payments/process.html', {'order': order})

@login_required
def payment_done(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'payments/done.html', {'order': order})

@login_required
def payment_cancelled(request):
    return render(request, 'payments/cancelled.html')

def send_order_confirmation_email(order):
    """Send order confirmation email to customer"""
    subject = f'Order Confirmation - Order #{order.id}'
    
    # Render email template
    html_message = render_to_string('emails/order_confirmation.html', {
        'order': order,
        'user': order.user,
    })
    
    plain_message = f"""
    Hi {order.user.username},
    
    Thank you for your order!
    
    Order Details:
    Order Number: #{order.id}
    Total Amount: ${order.total_amount}
    Status: {order.get_status_display()}
    
    Items:
    """
    
    for item in order.items.all():
        plain_message += f"\n- {item.product.name} x {item.quantity} = ${item.get_cost()}"
    
    plain_message += f"""
    
    Shipping Address:
    {order.address.full_name}
    {order.address.address_line1}
    {order.address.city}, {order.address.state} {order.address.postal_code}
    
    We'll send you another email when your order ships.
    
    Thank you for shopping with us!
    
    E-Store Team
    """
    
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@estore.com',
            [order.user.email],
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending customer email: {e}")

def send_admin_notification_email(order):
    """Send new order notification to admin"""
    subject = f'New Order Received - Order #{order.id}'
    
    admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@estore.com')
    
    message = f"""
    New Order Received!
    
    Order Details:
    Order Number: #{order.id}
    Customer: {order.user.username} ({order.user.email})
    Total Amount: ${order.total_amount}
    Payment Status: {order.payment_status}
    
    Items Ordered:
    """
    
    for item in order.items.all():
        message += f"\n- {item.product.name} x {item.quantity} = ${item.get_cost()}"
    
    message += f"""
    
    Shipping Address:
    {order.address.full_name}
    {order.address.phone}
    {order.address.address_line1}
    {order.address.city}, {order.address.state} {order.address.postal_code}
    
    Login to admin panel to process this order:
    http://127.0.0.1:8000/admin/orders/order/{order.id}/change/
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@estore.com',
            [admin_email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending admin email: {e}")
