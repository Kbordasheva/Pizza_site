from django.shortcuts import render
from pizza_products.models import PizzaProduct
from cart.forms import CartAddProductForm


def home(request):
    pizzas = PizzaProduct.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'pizzeria/home.html', locals())




