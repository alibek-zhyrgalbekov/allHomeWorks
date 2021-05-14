from django.shortcuts import render
from dz1.models import *

# Create your views here.


def get_products(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }

    for i in range(len(data['products'])):
        reviews = Review.objects.filter(product_id=data['products'][i].id)
        data['products'][i].reviews = len(reviews)

    return render(request, 'products.html', context=data)


def get_product(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product_id=id)

    data = {
        'product': product,
        'reviews': reviews
    }

    return render(request, 'product.html', context=data)