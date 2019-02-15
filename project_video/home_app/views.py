from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoClass
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home_app(request):
    video_all = VideoClass.objects.all().order_by('-update_at')
    return render(request, 'home_app/index.html', {'videos': video_all})

@login_required
def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
            return redirect('home_app')
    else:
        form = PostForm()
    return render(request, 'home_app/post_new.html', {'form': form})

def post_detail(request, post_id):
    post_num = get_object_or_404(VideoClass, id=post_id)
    video_all = VideoClass.objects.exclude(id=post_id)
    video_all = video_all.order_by('-update_at')[:4]
    return render(request, 'home_app/detail.html', {'videos': post_num, 'video_lain': video_all})

def search(request):
    queryset_list = VideoClass.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(judul__icontains=query)
    return render(request, 'home_app/search.html', {'videos': queryset_list})