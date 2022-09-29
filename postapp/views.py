from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author","blogmessage"]
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","blogmessage"]
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")  #redirects user to homepage after deletion
    
    
    
