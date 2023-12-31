from django.shortcuts import render
from django.views import View
from .models import Users
from .form import LoginForm, SignupForm, LostPasswordForm


class LoginView(View):
    from_class = LoginForm
    templated_name = 'accounts/login.html'
    def get(self, request):
        form = self.from_class()
        return render(request, self.templated_name, {'form': form})


class SignUpview(View):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class LostPasswordView(View):
    form_class = LostPasswordForm
    template_name = 'accounts/lost_password.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class ProfileUserView(View):
    template_name = 'accounts/profile.html'
    def get(self, request, *args, **kwargs):
        user = Users.objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, {'user': user})