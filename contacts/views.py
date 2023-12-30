from django.shortcuts import render
from django.views import View
from .models import ContactUs, AddressMe, CallMe


class ContactView(View):
    template_name = 'contacts/contact_us.html'
    def get(self, request):
        return render(request, self.template_name)