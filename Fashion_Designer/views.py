from django.shortcuts import render
from. models import Fashion_Designer_class

# Create your views here.
def Fashion_Designerinfo(request):
    fashion_designer=Fashion_Designer_class.objects.all()
    print(fashion_designer)

    context={

        "Fashion_Designer":fashion_designer
    }
    return render(request, 'Fashion_Designer/Fashion_Designerinfo.html',context)


from django.shortcuts import render
from. models import Fashion_Designer_class

from .forms import Fashion_Designer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Fashion_Designerinfo(request):
    Fashion_Designer=Fashion_Designer_class.objects.all()
    print(Fashion_Designer)

    context={

        "Fashion_Designer":Fashion_Designer
    }
    return render(request, 'Fashion_Designer/Fashion_Designerinfo.html',context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'Fashion_Designer/registration_Customer.html', context)

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


