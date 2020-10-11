from django.shortcuts import render
from. models import payment_class

from .forms import Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def PaymentInfo(request):
    Payment=payment_class.objects.all()
    print(Payment)

    context={

        "Payment":Payment
    }
    return render(request, 'Payment/PaymentInfo.html',context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }

    return render(request, 'Payment/registration_Payment.html', context)


@login_required
def make_Payment(request):
    message = ""
    form = Payment()

    if request.method == "POST":
        form = Payment(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            message = "Successfully added..."
            form = Payment()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'Payment/make_Payment.html', context)

