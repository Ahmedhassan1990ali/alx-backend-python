from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out before deletion to avoid issues
        user.delete()  # This triggers the post_delete signal
        return HttpResponse(status=204)

