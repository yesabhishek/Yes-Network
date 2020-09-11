from django.urls import path
from . import views
from .views import like_post
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView
from django.contrib.auth.models import User
from django.shortcuts import render



urlpatterns = [
    
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/',views.about, name='blog-about'),
    path('security/',views.security, name='blog-security'),
    path('like/',like_post, name='like-post'),
    
    
    
]


    