from django.db import models
from Customer .models import Customer_class
from order .models import order_class
# Create your models here.




class Product_Class(models.Model):
    Product_Id = models.IntegerField(blank=True, null=True)
    Order_No = models.IntegerField(blank=True,null=True)
    Product_details=models.CharField(max_length=20)
    Rate = models.IntegerField(blank=True,null=True)
    Catagories = models.CharField(max_length=50,
                                     choices=(('Cloth', 'Cloth'),
                                              ('Shoes', 'Shoes'),
                                              ('Cosmetics', 'Cosmetics')),
                                     default='Cloth')

    Product_image = models.ImageField(null='true')

    def __str__(self):
        return str(self.Product_Id) + " : " + self.Product_details



class order_product(models.Model):
    Customer=models.ForeignKey(Customer_class, on_delete=models.SET_NULL, null=True, default=1)
    Product= models.ForeignKey(Product_Class, on_delete=models.SET_NULL, null=True, default=1)
    order=models.ForeignKey(order_class, on_delete=models.SET_NULL, null=True, default=1)