from django.contrib import admin
from .models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
