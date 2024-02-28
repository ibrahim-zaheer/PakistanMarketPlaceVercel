from django.shortcuts import render
from django.http import HttpResponse
from item.models import Item,Category
from .forms import SignUpForm 
# Create your views here.
def index(request):
    #it will take first 6 items
    items = Item.objects.filter(is_sold = False)[0:6]
    category = Category.objects.all()

    return render(request,'index.html',{'items':items,'category':category})

def contact(request):
    return render(request,'contact.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')

    return render(request,'signup.html',{'form':form})