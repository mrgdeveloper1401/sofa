from django.urls import path
from .views import ProductCommentsView


app_name = 'comments'
urlpatterns = [
    path('best_comments', ProductCommentsView.as_view(), name='best_comments'),
]
