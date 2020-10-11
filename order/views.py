from django.shortcuts import render
from. models import order_class

from .forms import order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def orderinfo(request):
    order=order_class.objects.all()
    print(order)

    context={

        "order":order
    }
    return render(request, 'order/orderinfo.html',context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }

    return render(request, 'order/registration_order.html', context)


@login_required
def make_order(request):
    message = ""
    form = order()

    if request.method == "POST":
        form = order(request.POST,request.FILES)

    if form.is_valid():
        form.save()
        message = "Successfully added..."
        form = order()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'order/make_order.html', context)







