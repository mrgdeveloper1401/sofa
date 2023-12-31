from django.urls import path
from .views import HomeView, ProductImageSliderView, ProductImageView

app_name = 'products'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product_image_slider/<int:pk>', ProductImageSliderView.as_view(), name='product_image_slider'),
    path('product_image/<int:pk>', ProductImageView.as_view(), name='product_image'),
]