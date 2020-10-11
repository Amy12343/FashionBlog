from django.shortcuts import render
from. models import Customer_class

from .forms import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Customerinfo(request):
    Customer=Customer_class.objects.all()
    print(Customer)

    context={

        "Customer":Customer
    }
    return render(request, 'Customer/CustomerInfo.html',context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'Customer/registration_Customer.html', context)

@login_required
def insertCustomer(request):
    message = ""
    form = Customer()

    if request.method == "POST":
        form = Customer(request.POST,request.FILES)
        message = "you are wrong!!!!!"
        if form.is_valid():
            form.save()
            message = "Success..."
            form = Customer()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'Customer/insertCustomer.html', context)


