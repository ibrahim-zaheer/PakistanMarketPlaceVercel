from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from item.models import Item

class conversation(models.Model):
    item = models.ForeignKey(Item,related_name = "conversations",on_delete = models.CASCADE)
    # In the provided Django model definition, a ManyToManyField is 
    # used to establish a many-to-many relationship between the conversation model and the User model.
    members = models.ManyToManyField(User,related_name="conversations")
    created_at = models.DateTimeField(auto_now_add = True)
    # now whnever we use this model, modified_at will add the updated value
    modified_at = models.DateTimeField(auto_now = True)
    # so now the data will be arranges according to modified date
    class Meta:
        ordering = ('-modified_at',)

class conversationMessage(models.Model):
    # the related_name will be  used to access this field in html tag
    conversation = models.ForeignKey(conversation,related_name = "messages",on_delete = models.CASCADE)
    content = models.TextField()
        # now whnever we use this model, modified_at will add the updated value
    modified_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User,related_name = "created_messages",on_delete = models.CASCADE)

