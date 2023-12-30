from django.contrib import admin
from .models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass


# @admin.register(ImageSlider)
# class ImageSliderAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'create_at', 'update_at', 'is_active')
#     list_per_page = 20
#     search_fields = ('title', )
#     list_editable = ('is_active',)
#     prepopulated_fields = {'slug': ('title',)}