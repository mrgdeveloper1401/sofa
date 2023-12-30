from django.shortcuts import render
from django.views import View
from .models import Users
from .form import LoginForm


class LoginView(View):
    from_class = LoginForm
    templated_name = 'accounts/login.html'
    def get(self, request):
        form = self.from_class()
        return render(request, self.templated_name, {'form': form})


class SignUpview(View):
    form_class = ''
    template_name = 'accounts/signup.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})