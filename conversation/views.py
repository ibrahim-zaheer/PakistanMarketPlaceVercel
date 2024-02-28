from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from .models import conversation,conversationMessage
from .forms import  conversationMessageForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Item,pk = item_pk)
    # if the one that clicks the chat is the owner itself
    if item.created_by == request.user:
        return redirect('dashboard:index')
    

    #as you know the managing of the user is done in django itself, so it checks that person who clicked the chat with 
    # owner button is also logged in member
    conversations = conversation.objects.filter(item = item).filter(members = request.user.id)

    if conversations:
        pass #for redirecting to conversations

    if request.method == 'POST':
        form = conversationMessageForm(request.POST)

        if form.is_valid():
            conversations = conversation.objects.create(item = item)
            # for adding the user feild to member field of the model
            conversations.members.add(request.user)
            # for adding the owner of the product with the user at same time
            conversations.members.add(item.created_by)
            # remember we are actually using it as a group
            conversations.save()
        #    it means save the info of form but do not put it in database right now
            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversations
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail',pk = item_pk)
    else:
        form = conversationMessageForm()
    return render(request,'newConversation.html',{'form':form})           


# for showing messages recieved in inbox

@login_required
def inbox(request):
    conversations = conversation.objects.filter(members = request.user.id)
    

    return render(request,'inbox.html',{'conversations':conversations})


