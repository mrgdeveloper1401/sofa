from django.shortcuts import render
from django.views import View
from .models import Category


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories/categories.html', {'categories': categories})
