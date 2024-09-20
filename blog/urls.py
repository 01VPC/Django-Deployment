from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('',home,name="blog-home-page"),
    path('about',about,name="blog-about-page"),

    path('', PostListView.as_view(), name="blog-home-page"),
    path('post-new/', PostCreateView.as_view(), name="blog-new-page"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail-page"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update-page"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete-page")
]