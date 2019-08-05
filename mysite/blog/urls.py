from django.urls import path

from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogSignUpView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/signup', BlogSignUpView.as_view(), name='signup'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
]
