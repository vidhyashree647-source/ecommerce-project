from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

cart = {}

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product_id in cart:
        cart[product_id]['qty'] += 1
    else:
        cart[product_id] = {
            'product': product,
            'qty': 1
        }

    return redirect('/cart/')


def cart_view(request):
    total = 0

    for item in cart.values():
        total += item['product'].price * item['qty']

    return render(request, 'cart.html', {
        'cart_items': cart.values(),
        'total': total
    })


def place_order(request):
    for item in cart.values():
        Order.objects.create(
            product=item['product'],
            quantity=item['qty']
        )

    cart.clear()

    return render(request, 'order_success.html')