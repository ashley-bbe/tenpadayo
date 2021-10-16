from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import URLValidator
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    class Meta(object):
        db_table = 'product'
    
    product_name = models.CharField(
        'Product Name', max_length=100, blank=False, null=False)
    product_brand = models.CharField(
        'Product Brand', max_length=100, blank=False, null=True)
    product_type = models.CharField(
        'Product Type', max_length=100, blank=False, null=False)
    product_url = models.URLField(
        'Product URL', max_length=2000, blank=False, null=True)
    hair_type = models.CharField(
        'Hair Type', max_length=100, blank=False, null=False)
    hair_texture = models.CharField(
        'Hair Texture', max_length=100, blank=False, null=False)
    hair_porosity = models.CharField(
        'Hair Porosity', max_length=100, blank=False, null=False)
    image = CloudinaryField(
        'Image', blank= True, null= True)
    created_at = models.DateField(
        'Created DateTime', blank=True, auto_now_add=True)
    updated_at = models.DateField(
        'Updated DateTime', blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}'


class Wishlist(models.Model):
    class Meta(object):
        db_table = 'wishlist'

    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_brand = models.CharField(
        'Product Brand', max_length=100, blank=False, null=True)
    product_url = models.URLField(
        'Product URL', max_length=2000, blank=False, null=True)
    image = CloudinaryField(
        'Image', blank= True, null= True)
    created_at = models.DateField(
        'Created DateTime', blank=True, auto_now_add=True)
    updated_at = models.DateField(
        'Updated DateTime', blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.product}' 