from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app')        
    return render(request, 'signup/signup.html', {'form': form})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_app')
    else:
        form = PostForm()
    return render(request, 'home_app/post_new.html', {'form': form})