from django.db import models
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email= models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    price = models.DecimalField(default=0 , decimal_places=0 , max_digits=12)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
    star = models.IntegerField(default = 0, validators = [MinValueValidator(0)  , MaxValueValidator (5)])
    picture = models.ImageField(upload_to='upload/Product/')
    is_sale = models.BooleanField(default = False)
    sale_price = models.DecimalField( default = 0 ,decimal_places = 0, max_digits = 12)

    def __str__(self):
        return self.name
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    address= models.CharField(max_length=400, default='', blank=False)
    phone = models.CharField(max_length=20, blank=False )
    date = models.DateField(default=datetime.datetime.today() )
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
