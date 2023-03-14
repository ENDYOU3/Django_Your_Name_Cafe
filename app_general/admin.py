from django.contrib import admin
from .models import *

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ["title", "email", "comment_date", "user"]
    list_filter = ["comment_date"]
    search_fields = ["title"]
    
admin.site.register(Contact, ContactAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ["customer", "payment_method", "shipping_date", "status"]
    list_filter = ["status", "customer", "payment_method"]
    
admin.site.register(Shipping, ShippingAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "total_price", "shipping"]
    list_filter = ["shipping"]

admin.site.register(Order, OrderAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "country", "city", "user"]
    list_filter = ["country", "city", "user"]
    search_fields = ["first_name", "last_name"]

admin.site.register(Customer, CustomerAdmin)

