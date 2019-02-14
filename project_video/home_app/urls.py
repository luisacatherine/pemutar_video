from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app, name='home_app'),
    path('new_post', views.input_post, name='input_post'),
    path('video/<int:post_id>/', views.post_detail, name="post_detail")
    # url(r'^search/', views.search, name="search")
]