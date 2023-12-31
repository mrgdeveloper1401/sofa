from django.shortcuts import render
from django.views import View
from .models import ContactUs, AddressMe, CallMe, Services


class ContactView(View):
    template_name = 'contacts/contact_us.html'
    def get(self, request):
        return render(request, self.template_name)


class ServicesView(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request, 'contacts/services.html', {'services': services})
