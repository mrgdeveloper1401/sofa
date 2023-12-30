from django.shortcuts import render
from django.views import View
from .models import Product, Option, OptionValue, Attribute, AttributeValue


class HomeView(View):
    template_name = 'products/index.html'
    def get(self, request):
        return render(request, self.template_name)
    

class ProductImageSliderView(View):
    template_name = 'products/product_image_slider.html'
    def get(self, request, *args, **kwargs):
        produt = Product.objects.aget(pk=kwargs['pk'])
        product_image = produt.product_images.all()
        return render(request, self.template_name, {'product_image': product_image})
