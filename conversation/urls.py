from django.urls import path
from . import views

app_name = "conversation"

urlpatterns = [
    path('new/<int:item_pk>/',views.new_conversation,name='new'),
    path('',views.inbox,name='inbox'),
    # for finding detail of each inbox message
    path('<int:pk>',views.detail,name="detail")

]
