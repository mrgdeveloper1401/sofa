from django.shortcuts import render
from django.views import View
from .models import ContactUs, AddressMe, CallMe, Services, AboutUs, Faq


class ContactView(View):
    template_name = 'contacts/contact_us.html'
    def get(self, request):
        return render(request, self.template_name)


class ServicesView(View):
    def get(self, request):
        services = Services.objects.all()
        return render(request, 'contacts/services.html', {'services': services})


class AboutUsView(View):
    def get(self, request):
        about_us = AboutUs.objects.all()
        return render(request, 'contacts/about_us.html', {'about_us': about_us})
    

class FaqView(View):
    def get(self, request):
        faq = Faq.objects.all()
        return render(request, 'contacts/faq.html', {'faq': faq})