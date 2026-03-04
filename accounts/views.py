from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, AddressForm, ProfileForm
from .models import Address, Profile
from orders.models import Order

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('products:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'profile': profile,
        'addresses': addresses,
        'orders': orders
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
