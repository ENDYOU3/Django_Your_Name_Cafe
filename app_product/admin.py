from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'type','quantity','is_premium','promotion_end','created','updated']
	search_fields = ['title']
	list_filter = ['type','is_premium']

admin.site.register(Product, ProductAdmin)


class ProductTypeAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Product_Type, ProductTypeAdmin)