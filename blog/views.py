from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     context={
#         'posts' : Post.objects.all()
#     }
#     return render(request,"Html/home.html",context)

def about(request):
    return render(request,"Html/about.html")

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'Html/home.html'
    context_object_name = 'posts' #instead of sending the context we did it like this
    ordering = ["-date_posted"]
    

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'Html/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Html/post_form.html'
    # success_url = reverse_lazy('blog-home-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'Html/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False