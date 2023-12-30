from django.shortcuts import render
from django.views import View
from .models import Product, Option, OptionValue, Attribute, AttributeValue


class HomeView(View):
    template_name = 'products/index.html'
    def get(self, request):
        return render(request, self.template_name)