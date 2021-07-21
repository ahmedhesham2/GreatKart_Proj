from django.db import models
from category.models import Category

# Global variables
MAX_LENGTH = 255

# Create your models here.
class product(models.Model):
    product_name = models.CharField(unique=True , max_length= MAX_LENGTH)
    slug         = models.SlugField(unique=True , max_length= MAX_LENGTH)
    description  = models.CharField(max_length= MAX_LENGTH , blank= True)
    image        = models.ImageField(upload_to = "photos/products" , blank=True)
    price        = models.FloatField()
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self) :
        return self.product_name
    

