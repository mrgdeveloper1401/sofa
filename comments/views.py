from django.shortcuts import render
from django.views import View
from .models import ActiveComments, Answer, Comments, Questions


class ProductCommentsView(View):
    template_name = 'comments/comment_product.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)