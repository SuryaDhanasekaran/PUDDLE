from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#Creating Database models
class Category(models.Model):
    name = models.CharField(max_length=255)#only one field name with 255 characters maximum

    class Meta:
        ordering = ('name',)#order by name
        verbose_name_plural = 'Categories'#change the name of Category to Categories

    def __str__(self):#return the name of the category
        return self.name
    
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):#return the name of the category
        return self.name
