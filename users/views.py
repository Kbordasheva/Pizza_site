from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from orders.models import Order, ItemInOrder


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def account(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    my_orders = Order.objects.filter(user=user)
    orders_info = Order.objects.all()
    order_items = ItemInOrder.objects.all()
    return render(request, "users/account.html",
                  {"my_orders": my_orders, "order_items": order_items, "orders_info": orders_info})
