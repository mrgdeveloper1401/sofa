from django.contrib import admin
from .models import ContactUs, AddressMe, CallMe, Services, AboutUs, Faq


class CallMeInline(admin.TabularInline):
    model = CallMe
    extra = 0


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'body', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')
    search_fields = ('title', 'email', 'body')
    list_per_page = 20


@admin.register(AddressMe)
class AddressMe(admin.ModelAdmin):
    list_display = ('place_name', 'create_at', 'update_at')
    search_fields = ('place_name',)
    list_filter = ('create_at', 'update_at')
    inlines = (CallMeInline,)


@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
    list_display = ('mobile_phone', 'landing_phone', 'create_at', 'update_at')
    search_fields = ('mobile_phone', 'landing_phone')
    list_filter = ('create_at', 'update_at')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_at', 'update_at', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    list_filter = ('create_at', 'update_at', 'is_active')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'update_at', 'is_active')
    list_filter = ('create_at', 'update_at', 'is_active')
    list_per_page = 20
    search_fields = ('title',)
    list_editable = ('is_active',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'create_at', 'update_at', 'is_active')
    list_filter = ('create_at', 'update_at', 'is_active')
    search_fields = ('question', 'answer')
    list_per_page = 20
    list_editable = ('is_active',)