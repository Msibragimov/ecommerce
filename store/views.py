from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import datetime
import json

from .models import *
from .utils import cartData, guestOrder


def product_detail(request, pk):

    data = cartData(request)
    cartItems = data['cartItems']

    product = Product.objects.get(id=pk)
    product.viewed += 1
    product.save()
    context = {'product':product, 'cartItems': cartItems}
    return render(request, 'store/product.html', context)


def filter_by_category(request, pk):

    data = cartData(request)
    cartItems = data['cartItems']

    category = get_object_or_404(Category, pk=pk, parent=None)
    products = Product.objects.filter(category=category)
    context = {'products': products, 'cartItems': cartItems, 'category': category}
    return render(request, 'store/store.html', context)


def store(request):

    data = cartData(request)
    cartItems = data['cartItems']

    categories = Category.objects.filter(parent=None)
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'categories': categories}
    return render(request, 'store/store.html', context)


def cart(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(
            user=request.user, 
            name=data['user-form']['name'],
            phone=data['user-form']['phone']
        )
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['user-form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            country=data['shipping']['country'],
            city=data['shipping']['city'],
            address=data['shipping']['address'],
            ex_address=data['shipping']['ex_address'],
            zipcode=data['shipping']['zipcode']
        )

    return JsonResponse('Payment complete!', safe=False)
