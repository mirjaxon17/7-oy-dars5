from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/category/')
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class Products(models.Model):
    class PriceType(models.TextChoices):
        dollars = "USD", "$"
        sum = "UZS","sum"

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/product/')
    description = models.TextField()
    price = models.FloatField()
    made_in = models.CharField(max_length=50)
    price_type = models.CharField(max_length=10, choices=PriceType.choices,default=PriceType.sum, null=True)
    category = models.ManyToManyField(Category)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {self.price_type} - {self.price}  {self.category}"

class Search(models.Model):
    field = models.CharField(max_length=100)

    def __str__(self):
        return self.field
