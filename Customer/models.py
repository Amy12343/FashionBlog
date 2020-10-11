from django.db import models



# Create your models here.
class Address(models.Model):
    House_No=models.IntegerField(blank=True,null=True, default="")
    Street_Address = models.CharField(max_length=200)
    Postal_Address = models.CharField(max_length=200)
    Postal_Code = models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    def __str__(self):
        return str(self.House_No) + " ," + self.Street_Address + " ," + self.City


class Customer_class(models.Model):
    Customer_Id=models.IntegerField(blank=True,null=True)
    Name = models.CharField(max_length=200, default= "")
    Email = models.EmailField(max_length=200,unique=True)
    phone_No = models.IntegerField(blank=True, null=True)
    Status=models.CharField(max_length=200)


    Address=models.ForeignKey(Address, on_delete=models.CASCADE,default=1)

    def __str__(self):
          return str(self.Customer_Id) + " : " + self.Name
