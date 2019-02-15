from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from home_app.models import VideoClass

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app')
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

def profile(request):
    user_now = User.objects.get(username=request.user.username)
    querylist = VideoClass.objects.all()
    query = request.user.username
    querylist = querylist.filter(posted_by__contains=query)
    return render(request, 'signup/profile.html', {'user': user_now, 'videos': querylist})

def profile_umum(request, username):
    user = User.objects.get(username=username)
    querylist = VideoClass.objects.all()
    query = username
    querylist = querylist.filter(posted_by__contains=query)
    return render(request, 'signup/profile_umum.html', {'videos': querylist, 'user': user})