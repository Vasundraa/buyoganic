from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Productshop(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productshop_images/')
    category = models.CharField(max_length=255, default="NULL")
    is_new = models.BooleanField(default=False)

    class Meta:
        ordering = ['-price']

    def __str__(self):
        return self.name
