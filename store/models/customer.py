from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Customer(models.Model):
    first_name= models.CharField(max_length=30, blank=True, null=True)
    last_name= models.CharField(max_length=40)
    email = models.EmailField()
    Password = models.CharField(max_length=200)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False