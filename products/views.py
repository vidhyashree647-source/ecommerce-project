from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

cart = []

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart.append(product)
    return redirect('/cart/')


def cart_view(request):
    total = sum(item.price for item in cart)

    return render(request, 'cart.html', {
        'cart_items': cart,
        'total': total
    })


def place_order(request):
    for product in cart:
        Order.objects.create(product=product)

    cart.clear()

    return render(request, 'order_success.html')