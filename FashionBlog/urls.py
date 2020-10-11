"""FashionBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Users import views as user_views
from Customer import views as Customer_views
from Product import views as Product_views
from order import views as order_views
from Fashion_Designer import views as Fashion_Designer_views
from Payment import views as Payment_views


admin.site.site_header = "Fashion Blog Admin"
admin.site.site_title = "Fashion Blog Portal"
admin.site.index_title = "Welcome to our Fashion Blog"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Customer/', Customer_views.Customerinfo, name='Customer'),
    path('insertCustomer/', Customer_views.insertCustomer, name='insertCustomer'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('Product/', Product_views.Productinfo, name='Product'),
    path('uploadProduct/', Product_views.uploadProduct, name='uploadProduct'),

    path('registration_Customer/', Customer_views.registration, name='registration'),


    path('order/', order_views.orderinfo,name='order'),
    path('make_order/', order_views.make_order, name='make_order'),

    path('Payment/', Payment_views.PaymentInfo, name='Payment'),
    path('make_Payment/', Payment_views.make_Payment, name='make_Payment'),

    path('Fashion_Designer/', Fashion_Designer_views.Fashion_Designerinfo,name='Fashion_Designer'),
    path('Product/<int:product_id>', Product_views.showDetails, name='detail_view'),




    path('profile/', user_views.show_profile, name='show_profile'),
    path('createprofile/', user_views.create_profile, name='create_profile')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
