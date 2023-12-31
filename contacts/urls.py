from django.urls import path
from .views import ContactView, ServicesView, AboutUsView, FaqView

app_name = 'contact_us'
urlpatterns = [
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    path('services', ServicesView.as_view(), name='services'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('faq/', FaqView.as_view(), name='faq')
]
