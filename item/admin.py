from django.contrib import admin
from .models import Category,Item
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','description','is_sold']    


admin.site.register(Category,CategoryAdmin)


admin.site.register(Item)