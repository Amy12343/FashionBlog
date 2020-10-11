from django.shortcuts import render
from. models import Product_Class

from .forms import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Productinfo(request):
    Product=Product_Class.objects.all()
    if request.method == 'POST':
        Product = Product_Class.objects.filter(Product_Id__icontains=request.POST['search'])
        Catagories = Product_Class.objects.filter(Catagories__icontains=request.POST['search'])
        Rate = Product_Class.objects.filter(Rate__icontains=request.POST['search'])

        Product = Product | Catagories | Rate  # C = A U B set operation
        print(Product)

    context={

        "Product":Product
    }
    return render(request, 'Product/ProductInfo.html',context)





def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'Product/registration_Product.html', context)

def showDetails(request, product_id):
    does_exists = True
    searched_product = Product_Class.objects.filter(id=product_id)
    if searched_product == 0:
        does_exists = False
        context = {'does_exist': does_exists,

                   }
    else:
        search = searched_product[0]
        context = {'does_exist': does_exists,
                   'search': search
                   }



    return render(request, 'Product/detail_product_view.html', context)













@login_required
def uploadProduct(request):
    message = ""
    form = Product()

    if request.method == "POST":
        form = Product(request.POST,request.FILES)
        message = "you are wrong!!!!!"
        if form.is_valid():
            form.save()
            message = "Successfully Product uploaded..."
            form = Product()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'Product/uploadProduct.html', context)

