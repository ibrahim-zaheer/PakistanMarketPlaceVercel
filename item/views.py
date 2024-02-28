from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Item
#add this so login will be require to use certain view function
from django.contrib.auth.decorators import login_required
from .forms import newItemForm,editItemForm
# import this to allow you to search even with different fields like description
from django.db.models import Q
# Create your views here.

def detail(request,pk):
    item = get_object_or_404(Item,pk= pk)
    # to show related objects of the same category and we use [0:3] to display three items at a time
    related_items = Item.objects.filter(category = item.category,is_sold = False).exclude(pk = pk)[0:3]
    return render(request,'detail.html',{'item':item,'related_items':related_items})

@login_required
def new(request):
    if request.method == 'POST':
        form = newItemForm(request.POST,request.FILES)

        if form.is_valid:
            #since we are going to store an image as well we fist save the formn and then save database
            item = form.save(commit= False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',pk = item.id)
    else:
        form = newItemForm()
    return render(request,'form.html',{'form':form,'title':'new Item'})

@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    if request.method == 'POST':
        form = editItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            #since we are editing the form so form is already saved so no need to write extra code as we did
            # for new method
            item.save()
            return redirect('item:detail',pk = item.id)
    else:
        # the reason we write instace is if we don't we will only see an empty form so we fill it with existing 
        # or old form data
        form = editItemForm(instance=item)
    return render(request,'form.html',{'form':form,'title':'edit Item'})

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    item.delete()

    return redirect('dashboard:index')

# add this code to allow you to search items in the market place
def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    # if category is clicked
    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains=query )| Q(description__icontains = query))
    
    return render(request,'items.html',{"items":items,"query":query,"categories":categories,'category_id':int(category_id)})
