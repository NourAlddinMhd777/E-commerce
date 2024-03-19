from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Ecommerce Products Model 2/3
class Category(models.TextChoices): 
    tech = "Tehnology"
    kids = "Kids"
    furniture = "Furniture"
    clothes = "Clothes"
    books = "Books"
    elegance_and_beauty = "Elegance_and_Beauty"
# Ecommerce Products Model 2/3__END
# Ecommerce Products Model 3/3__in Terminal:
    #python manage.py makemigrations.....(1)
    #python manage.py migrate.....(2)
    #next step : Ecommerce Products Views, Urls  in admin.py 

    
# Ecommerce Products Model 1/3
class Product(models.Model):
    name = models.CharField(max_length=200,default = "",blank = False)
    discraption = models.CharField(max_length=1000,default = "",blank = False)
    price = models.DecimalField(max_digits=5, decimal_places=2 ,default = 0,blank = False)
    category = models.CharField(max_length = 40,choices = Category.choices)
    brand = models.CharField(max_length = 100,default ="",blank = False)
    ratings = models.DecimalField(max_digits=3, decimal_places=2 ,default = 0)
    stock = models.IntegerField(default = 0)
    createAt= models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Ecommerce Products Model 1/3__END
# Ecommerce Products Model 2/3__in models.py

    
# Django | Review & Rating API 1/
class Review (models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="review_product",null = True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2 ,default = 0)
    comment = models.CharField(max_length=1000,default = "",blank = False)
    createAt= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
# Django | Review & Rating API 1/ __END
# Django | Review & Rating API 2/ in serializers.py
    
    
# Django | Review & Rating API 3/
# Django | Review & Rating API 3/ __END
# Django | Review & Rating API 4/ in .py

