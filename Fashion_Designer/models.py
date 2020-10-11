from django.db import models

# Create your models here.

class Fashion_Designer_class(models.Model):
    Designer_id=models.IntegerField(blank=True,null=True)
    Name=models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phn_no = models.IntegerField(blank=True)
    Address = models.CharField(max_length=100)


    def __str__(self):
        return str(self.Designer_id) + " : " + self.Name

