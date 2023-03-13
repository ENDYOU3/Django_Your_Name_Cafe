from django.urls import path
from app_product import views

urlpatterns = [
    path("", views.All_Products, name="products-page"),
    path("<slug>", views.One_Product, name="product-page"),
    path("coffee/", views.All_Coffee, name="products_coffee-page"),
    path("tea/", views.All_Tea, name="products_tea-page"),
    path("milk/", views.All_Milk, name="products_milk-page"),
    path("cake/", views.All_Cake, name="products_cake-page"),
]
