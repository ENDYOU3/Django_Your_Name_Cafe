from django.urls import path
from app_product import views

urlpatterns = [
    path("", view=views.All_Products, name="products-page"),
    path("<slug>", view=views.One_Product, name="product-page"),
    path("coffee/", view=views.All_Coffee, name="products_coffee-page"),
    path("tea/", view=views.All_Tea, name="products_tea-page"),
    path("milk/", view=views.All_Milk, name="products_milk-page"),
    path("cake/", view=views.All_Cake, name="products_cake-page"),
]
