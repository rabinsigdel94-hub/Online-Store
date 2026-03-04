from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from .models import Product, Category
from reviews.models import Review

def home(request):
    featured_products = Product.objects.filter(available=True)[:8]
    categories = Category.objects.filter(parent=None)[:6]
    context = {
        'featured_products': featured_products,
        'categories': categories
    }
    return render(request, 'products/home.html', context)

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    category = request.GET.get('category')
    if category:
        products = products.filter(category__slug=category)
    
    sort = request.GET.get('sort', 'name')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating
    }
    return render(request, 'products/detail.html', context)

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    context = {'category': category, 'products': products}
    return render(request, 'products/category.html', context)

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query),
        available=True
    )
    context = {'products': products, 'query': query}
    return render(request, 'products/search.html', context)
