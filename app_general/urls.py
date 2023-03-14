from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.Home, name="home-page"),
    path("about_user/", views.AboutUser, name="about_user-page"),
    path("register_user/", views.RegisterUser, name="register_user-page"),
    path("contact/", views.ContactMessage, name="contact-page"),
    path("shopping_cart/", views.show_item_in_cart, name="show_item_in_cart-page"),
    re_path(r"^add_to_cart/(?P<slug>[\w-]+)/$", views.add_to_cart, name="add_to_cart-page"),
    re_path(r"^delete_cart/(?P<slug>[\w-]+)/$", views.delete_item, name="delete_product-page"),
    path("order/", views.show_order, name="order-page"),
    path("add_customer/", views.add_customer, name="add_customer-page"),
    path("order/<customer_id>/", views.select_customer, name="select_customer-page"),
    path("order/del_customers/<customer_id>", views.delete_customer, name="del_customer-page"),
    path("history_shopping/", views.history_shopping, name="history_shop-page"),
    path("history_shopping/<customer_id>/", views.select_history, name="select_history-page"),
    path("thank_you/", views.Thankyou, name="thank_you-page"),
]