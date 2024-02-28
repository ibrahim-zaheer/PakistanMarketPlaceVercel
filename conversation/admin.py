from django.contrib import admin
from .models import conversation,conversationMessage
# Register your models here.

admin.site.register(conversationMessage)
admin.site.register(conversation)
