from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item
# Create your views here.

#we use login required to first let user log in and then access the data
@login_required
def index(request):
    #this is power of django, where you don't need to create a separate funtion to filter items based on user pk
    #let django handle it
    items = Item.objects.filter(created_by = request.user)
    return render(request,'dashboard.html',{'items':items})


