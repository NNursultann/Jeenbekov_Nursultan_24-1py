from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    rate = models.FloatField(default=0.0)

class Review(models.Model):
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
