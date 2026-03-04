from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.cart import Cart
from accounts.models import Address

@login_required
def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, 'Your cart is empty')
        return redirect('cart:detail')
    
    if request.method == 'POST':
        address_id = request.POST.get('address')
        address = get_object_or_404(Address, id=address_id, user=request.user)
        
        order = Order.objects.create(
            user=request.user,
            address=address,
            total_amount=cart.get_total_price()
        )
        
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        
        cart.clear()
        return redirect('payments:process', order_id=order.id)
    
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'orders/create.html', {'cart': cart, 'addresses': addresses})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/list.html', {'orders': orders})
