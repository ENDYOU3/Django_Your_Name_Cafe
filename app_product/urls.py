from django.urls import path
from app_product import views

urlpatterns = [
    path("", view=views.show_all_products, name="products-page"),
    path("<slug>", view=views.show_product, name="product-page"),
    path("coffee/", view=views.show_only_coffee, name="products_coffee-page"),
    path("tea/", view=views.show_only_tea, name="products_tea-page"),
    path("milk/", view=views.show_only_milk, name="products_milk-page"),
    path("cake/", view=views.show_only_cake, name="products_cake-page"),
]
