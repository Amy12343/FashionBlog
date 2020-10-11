from django.db import models

# Create your models here.
class payment_class(models.Model):
    payment_Id = models.IntegerField(blank=True,null=True)
    payment_type = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)



    def __str__(self):
        return str(self.payment_Id) + " : " + self.payment_type
