from django.shortcuts import render, redirect

# Create your views here.
def home_app(request):
    return render(request, 'home_app/index.html', {})