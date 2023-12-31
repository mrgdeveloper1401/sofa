from django.shortcuts import render
from django.views import View
from .models import Category


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'contacts/category.html', {'categories': categories})
