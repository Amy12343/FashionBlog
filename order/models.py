from django.db import models
from Customer .models import Customer_class
from Payment .models import payment_class
# Create your models here.

class order_class(models.Model):
    order_no =models.IntegerField(blank=True,null=True)
    order_Date=models.DateField(blank=True,null=True)
    order_details = models.CharField(max_length=200,default= "")
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )

    order_Status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')


    order_image = models.ImageField(null='true')

    Customer = models.ForeignKey(Customer_class, on_delete=models.SET_NULL, null=True, default=1)
    Payment = models.ForeignKey(payment_class, on_delete=models.SET_NULL, null=True, default=1)

    def __str__(self):
        return str(self.order_no) + " : " + self.order_Status