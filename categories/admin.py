from django.contrib import admin
from .models import Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'parent', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'create_at', 'update_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'category', 'is_active')
    search_fields = ('brand_name',)
    list_filter = ('is_active', 'create_at', 'update_at')
    list_per_page = 20
