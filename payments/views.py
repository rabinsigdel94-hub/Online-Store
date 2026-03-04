from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
from .models import Payment
from orders.models import Order

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
        
        messages.success(request, 'Payment successful!')
        return redirect('payments:done', order_id=order.id)
    
    return render(request, 'payments/process.html', {'order': order})

@login_required
def payment_done(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'payments/done.html', {'order': order})

@login_required
def payment_cancelled(request):
    return render(request, 'payments/cancelled.html')
