from django.shortcuts import render
from django.views import View
from .models import CommentPost, Post


class PostView(View):
    template_name = 'blog/all_posts.html'
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(is_active=True)
        return render(request, self.template_name, {'all_post': post})
    

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        return render(request, 'blog/post_details.html', {'post': post})