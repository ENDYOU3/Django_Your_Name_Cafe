from django.shortcuts import render
from app_product.models import Product
from app_product.forms import *

# Create your views here.


def All_Products(request):
    all_products = Product.objects.order_by("-is_premium")
    product_quantity = len(all_products)
    context = {"products": all_products, "product_quantity": product_quantity}
    return render(request, "app_product/products.html", context)


def One_Product(request, slug):
    thisProduct = None
    try:
        thisProduct = Product.objects.get(slug=slug)
    except:
        print("Not Found!")
    context = {"thisProduct": thisProduct}
    return render(request, "app_product/product.html", context)


# Note type >> 1=coffee, 2=tea, 3=milk, 4=cake

def All_Coffee(request):
    all_products = Product.objects.filter(type=1).order_by("-is_premium")
    product_quantity = len(all_products)
    context = {"products": all_products, "product_quantity": product_quantity}
    return render(request, "app_product/coffee.html", context)


def All_Tea(request):
    all_products = Product.objects.filter(type=2).order_by("-is_premium")
    product_quantity = len(all_products)
    context = {"products": all_products, "product_quantity": product_quantity}
    return render(request, "app_product/tea.html", context)


def All_Milk(request):
    all_products = Product.objects.filter(type=3).order_by("-is_premium")
    product_quantity = len(all_products)
    context = {"products": all_products, "product_quantity": product_quantity}
    return render(request, "app_product/milk.html", context)


def All_Cake(request):
    all_products = Product.objects.filter(type=4).order_by("-is_premium")
    product_quantity = len(all_products)
    context = {"products": all_products, "product_quantity": product_quantity}
    return render(request, "app_product/cake.html", context)
