from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_general.forms import *
from django.contrib import messages
from app_product.models import Product
from django.contrib.auth.models import User

# Create your views here.


def show_home_page(request):
	return render(request, "app_general/home.html")


@login_required
def show_item_in_cart(request):
	product_list = request.session.get("product_list") or []
	total_qty = 0
	total_price = 0
	add_shipping_cost = False
	# Total price and quantity of product
	for item in product_list:
		total_price += item.get("total_price")
		total_qty += item.get("qty")
	request.session["total_qty"] = total_qty
	request.session["total_price"] = total_price
	request.session["add_shipping_cost"] = add_shipping_cost
	if request.method == "POST":
		return HttpResponseRedirect(reverse("app_general:order-page", kwargs={}))
	context = {"product_list": product_list}
	return render(request, "app_general/shopping_cart.html", context)


@login_required
def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	product_list = request.session.get("product_list") or []
	item_in_cart = False
	# Update product quantity in the cart
	for item in product_list:
		if item.get("slug") == product.slug:
			if product.quantity > item.get("qty"):
				item["qty"] += 1
				item["total_price"] = item.get("price") * item.get("qty")
			item_in_cart = True 
	# Add new product into chart
	if not item_in_cart: 
		if product.special_price is not None:
			product_price = product.special_price
		else:
			product_price = product.price
		product_list.append(
			{
				"slug": product.slug,
				"title": product.title,
				"price": product_price,
				"qty": 1,
				"total_price": product_price,
			}
		)
	request.session["product_list"] = product_list
	return HttpResponseRedirect(reverse("app_general:show_item_in_cart-page"))


def delete_item(request, slug):
	product_list = request.session.get("product_list")
	for i in range(len(product_list)):
		if product_list[i]["slug"] == slug:
			del product_list[i]
			break
	request.session["product_list"] = product_list
	return HttpResponseRedirect(reverse("app_general:show_item_in_cart-page"))


@login_required
def show_order(request):
	username = request.user.username
	user = User.objects.get(username=username)
	all_customer = Customer.objects.filter(user=user)
	shipping_method = []
	# Add shipping cost to the total price
	shipping_cost = 40
	request.session["shipping_cost"] = shipping_cost
	if not request.session["add_shipping_cost"]:
		request.session["total_price"] += request.session["shipping_cost"]
		request.session["add_shipping_cost"] = True
	count_item = len(request.session["product_list"])
	if request.method == "POST":
		# Check exception when place order and not selecting an address
		try:
			request.session["customer"]
			form = OrderDetailForm(request.POST)
			if form.is_valid():
				shipping_method.append({
					"note": form.cleaned_data["note"],
					"payment_method": form.cleaned_data["payment_method"]
				})
				# Add new shipping to database
				new_shipping = Shipping()
				new_shipping.customer = Customer.objects.get(id=request.session["customer_id"])
				new_shipping.payment_method = shipping_method[-1].get("payment_method")
				new_shipping.note = shipping_method[-1].get("note")
				new_shipping.save()
				# Add new order to database
				product_list = request.session["product_list"]
				for idx, item in enumerate(product_list):
					product = get_object_or_404(Product, slug=item.get("slug"))
					new_order = Order()
					new_order.product = product
					new_order.quantity = item.get("qty")
					new_order.total_price = item.get("total_price")
					new_order.shipping = Shipping.objects.all().last()
					new_order.save()
					# Update quantity of product in stock
					product.quantity -= new_order.quantity
					product.save()
			# Reset value in session
			request.session["total_qty"] = []
			request.session["product_list"] = []
			request.session["total_price"] = []
			return HttpResponseRedirect(reverse('app_general:thank_you-page'))
		except:
			messages.error(request, "An error occurred when we tried to set your shipping address. Please try again.")
			return HttpResponseRedirect(reverse('app_general:order-page'))
	else:
		form = OrderDetailForm()
	context = {
		"count_item": count_item,
		"all_customer": all_customer,
		"count_customer": len(all_customer),
		"form": form
	}
	return render(request, "app_general/order.html", context)


@login_required
def add_customer(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			customer = []
			customer.append({
				"first_name": form.cleaned_data["first_name"],
				"last_name": form.cleaned_data["last_name"],
				"country": form.cleaned_data["country"],
				"city": form.cleaned_data["city"],
				"address": form.cleaned_data["address"],
				"phone": form.cleaned_data["phone"],
			})
		# Add new customer to database
		new_customer = Customer()
		username = request.user.username
		new_customer.user = User.objects.get(username=username)
		new_customer.first_name = customer[0].get("first_name")
		new_customer.last_name = customer[0].get("last_name")
		new_customer.country = customer[0].get("country")
		new_customer.city = customer[0].get("city")
		new_customer.address = customer[0].get("address")
		new_customer.phone = customer[0].get("phone")
		new_customer.save()
		messages.success(request, "Add new address complete!")
		request.session["customer"] = customer
		request.session["customer_id"] = Customer.objects.all().last().id
		return HttpResponseRedirect(reverse("app_general:order-page"))
	else:
		form = CustomerForm()
	context = {"form": form}
	return render(request, "app_general/add_customer.html", context)


def select_customer(request, customer_id):
	customers = Customer.objects.get(id=customer_id)
	customer = []
	customer.append(
		{
			"first_name": customers.first_name,
			"last_name": customers.last_name,
			"country": customers.country,
			"city": customers.city,
			"address": customers.address,
			"phone": customers.phone,
		}
	)
	request.session["customer"] = customer
	request.session["customer_id"] = customer_id
	return HttpResponseRedirect(reverse("app_general:order-page", kwargs={}))


def delete_customer(request, customer_id):
	del_customer = Customer.objects.get(id=customer_id)
	del_customer.delete()
	request.session["customer"] = []
	return HttpResponseRedirect(reverse("app_general:order-page", kwargs={}))


@login_required
def history_shopping(request):
	username = request.user.username
	user = User.objects.get(username=username)
	all_customer = Customer.objects.filter(user=user)
	try:
		customer_id = request.session["customer_id"]
		customer = Customer.objects.filter(id=customer_id)
		# join table
		order_list = Order.objects.filter(shipping_id__customer_id=customer_id, shipping_id__status="Approve").values_list("shipping_id", "shipping_id__shipping_date", "product_id__title", "quantity", "total_price")
		status = True
		context = {
	     	"all_customer": all_customer,
			"count_customer": len(all_customer), 
			"customer": customer,
			"order_list": order_list,
			"order_qty": len(order_list),
			"status": status
			}
		return render(request, "app_general/history_shopping.html", context)
	except:
		status = False
		context = {
			"count_customer": len(all_customer),  
			"all_customer": all_customer,
			"status": status
			}
		return render(request, "app_general/history_shopping.html", context)


def select_history(request, customer_id):
	request.session["customer_id"] = customer_id
	return HttpResponseRedirect(reverse("app_general:history_shop-page", kwargs={}))


@login_required
def show_thank_you_page(request):
	return render(request, "app_general/thank_for_shopping.html")


@login_required
def contact_message(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			new_contact = Contact()
			username = request.user.username
			new_contact.user = User.objects.get(username=username) 
			new_contact.title = form.cleaned_data["title"]
			new_contact.email = form.cleaned_data["email"]
			new_contact.description = form.cleaned_data["description"]
			new_contact.save()
			messages.success(request, f"{username}, Thanks for your feedback.")
			return HttpResponseRedirect("app_general:home-page")
	else:
		form = ContactForm()
	context = {"form": form}
	return render(request, "app_general/contact.html", context)