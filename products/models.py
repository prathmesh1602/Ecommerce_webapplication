from django.db import models
from base.models import BaseModel



class Catagory(BaseModel):
    caragory_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    caragory_image = models.ImageField(upload_to="catgories")

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE ,related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()

class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="product")


