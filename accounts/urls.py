from django.urls import path
from .views import LoginView, SignUpview, LostPasswordView, ProfileUserView


app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpview.as_view(), name='signup'),
    path('lostpassword/', LostPasswordView.as_view(), name='lost_password'),
    path('profile/<int:pk>/', ProfileUserView.as_view(), name='profile'),
]