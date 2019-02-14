from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoClass
from .forms import PostForm

# Create your views here.
def home_app(request):
    video_all = VideoClass.objects.all().order_by('-update_at')
    return render(request, 'home_app/index.html', {'videos': video_all})

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

def post_detail(request, post_id):
    post_num = get_object_or_404(VideoClass, id=post_id)
    video_all = VideoClass.objects.exclude(id=post_id)
    video_all = video_all.order_by('-update_at')
    return render(request, 'home_app/detail.html', {'videos': post_num, 'video_lain': video_all})

# def search(request):        
#     if request.method == 'GET': # this will be GET now      
#         book_name =  request.GET.get('search') # do some research what it does       
#         try:
#             status = Add_prod.objects.filter(bookname__icontains=book_name) # filter returns a list so you might consider skip except part
#         return render(request,"search.html",{"books":status})
#     else:
#         return render(request,"search.html",{})