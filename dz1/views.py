from django.contrib import auth
from django.shortcuts import render, redirect
from dz1.forms import CategoryForm, UserCreationForm, LoginForm, ProductForm
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


def prod(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
        else:
            return render(request, 'prod.html', context={
                'form': form.errors
            })
    data = {
        'form': CategoryForm
    }
    return render(request, 'prod.html', context=data)


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', context={'form': UserCreationForm})

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/admin/')
        else:
            return render(request, 'register.html', context={'form': form})


def login(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
            redirect('/')
            return render(request, 'login.html', context={
                'user': user,
                'categories': categories
            })

    data = {
        'categories': categories,
        'form': LoginForm
    }

    return render(request, 'login.html', context=data)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            data = {
                'form': ProductForm(),
                'username': auth.get_user(request).username
            }
            return render(request, 'add_product.html', context=data)

    data = {
        'form': ProductForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'add_product.html', context=data)
