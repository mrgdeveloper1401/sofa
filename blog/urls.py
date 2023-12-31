from django.urls import path
from .views import PostView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('all_posts/', PostView.as_view(), name='all_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
