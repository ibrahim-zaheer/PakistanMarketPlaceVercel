from django.urls import path
from . import views
#this will help us for cross movement between the apps because just the name won't be enough to 
# differentiate in html hyper links
app_name = 'item'
urlpatterns = [
    path('<int:pk>',view=views.detail,name='detail'),
    
    path('new/',view=views.new,name='new'),
    path('<int:pk>/delete/',view=views.delete,name='delete'),
     path('<int:pk>/edit/',view=views.edit,name='edit'),
     path('',views.items,name='items')

]
