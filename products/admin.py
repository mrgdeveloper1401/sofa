from django.contrib import admin
from .models import Product, Option, OptionValue, Attribute, AttributeValue


class OptionInline(admin.TabularInline):
    model = Option
    extra = 0


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0


class OptionValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


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
