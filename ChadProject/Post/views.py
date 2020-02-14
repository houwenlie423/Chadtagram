from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post, Comment

class PostList(ListView) :
  model = Post
  template_name = 'Post/PostList.html'
  context_object_name = 'post_list'

  def get_queryset(self):
      return Post.objects.all().order_by('-created_at')
  
  

class PostDetail(DetailView) :
  model = Post
  template_name = 'Post/PostDetail.html'
  context_object_name = 'post'
  