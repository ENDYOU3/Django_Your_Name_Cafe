from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", view=views.Home, name="home-page"),
    path("contact/", view=views.ContactMessage, name="contact-page"),
    path("shopping_cart/", view=views.show_item_in_cart, name="show_item_in_cart-page"),
    re_path(r"^add_to_cart/(?P<slug>[\w-]+)/$", view=views.add_to_cart, name="add_to_cart-page"),
    re_path(r"^delete_cart/(?P<slug>[\w-]+)/$", view=views.delete_item, name="delete_product-page"),
    path("order/", view=views.show_order, name="order-page"),
    path("add_customer/", view=views.add_customer, name="add_customer-page"),
    path("order/<customer_id>/", view=views.select_customer, name="select_customer-page"),
    path("order/del_customers/<customer_id>", view=views.delete_customer, name="del_customer-page"),
    path("history_shopping/", view=views.history_shopping, name="history_shop-page"),
    path("history_shopping/<customer_id>/", view=views.select_history, name="select_history-page"),
    path("thank_you/", view=views.Thankyou, name="thank_you-page"),
]