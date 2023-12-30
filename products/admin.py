from django.contrib import admin
from .models import Product, Option, OptionValue, Attribute, AttributeValue, ProductImage


class OptionInline(admin.TabularInline):
    model = Option
    extra = 0


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0


class OptionValueInline(admin.TabularInline):
    model = OptionValue
    extra = 0


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('en_name', 'category', 'brand', 'is_active', 'is_stock')
    prepopulated_fields = {'slug': ('en_name',)}
    list_per_page = 20
    search_fields = ('en_name', 'fa_name', 'create_at', 'update_at')
    inlines = (ProductImageInline, AttributeValueInline, OptionValueInline)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(OptionValue)
class OptionValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
