"""djangoProjectdz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dz1 import views as dz1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', dz1.get_products),
    path('products/<int:id>/', dz1.get_product),
    path('prod/', dz1.prod),
    path('register/', dz1.register),
    path('login/', dz1.login),
    path('add_product/', dz1.add_product),

]
