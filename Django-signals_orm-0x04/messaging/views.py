from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpResponse
from .models import Message

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out before deletion to avoid issues
        user.delete()  # This triggers the post_delete signal
        return HttpResponse(status=204)


def thread_view(request, message_id):
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver'),
        pk=message_id
    )
    return render(request, 'messaging/thread.html', {
        'root_message': message,
        'thread': message.get_thread()
    })

def inbox_view(request):
    conversations = Message.objects.get_user_conversations(request.user)
    return render(request, 'messaging/inbox.html', {
        'conversations': conversations
    })


@login_required
def thread_view(request, message_id):
    # Get message with sender=request.user check
    message = get_object_or_404(
        Message.objects.filter(
            Q(sender=request.user) | Q(receiver=request.user)
        ).select_related('sender', 'receiver'),
        pk=message_id
    )
    return render(request, 'messaging/thread.html', {
        'root_message': message,
        'thread': message.get_thread()
    })

@login_required
def inbox_view(request):
    # Explicitly filter messages where user is sender or receiver
    conversations = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user),
        parent_message__isnull=True
    ).select_related(
        'sender', 'receiver'
    ).prefetch_related(
        'replies'
    ).order_by('-timestamp')
    
    return render(request, 'messaging/inbox.html', {
        'conversations': conversations
    })

