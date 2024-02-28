from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)
    class Meta:
        ordering = ('name',)
    def __str__(self)    :
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category,related_name = 'items',on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True,null = True)
    price = models.FloatField()
    image = models.ImageField(upload_to="img/%y",blank=True,null=True)
    #we will use this to display only those itmes that are not sold, means helps us in filtering
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User,related_name = 'items',on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add = True)
    def __str__(self)    :
        return self.name

