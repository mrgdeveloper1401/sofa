from django.urls import path
from .views import ContactView, ServicesView

app_name = 'contact_us'
urlpatterns = [
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    path('services', ServicesView.as_view(), name='services'),
]
