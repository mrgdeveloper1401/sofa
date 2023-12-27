from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from .manaers import ActiveManager


class Product(Create, Update):
    en_name = models.CharField(_('نام انگلیسی'), max_length=155, db_index=True)
    fa_name = models.CharField(_('نام فارسی'), max_length=155)
    slug = models.SlugField(_('اسلاگ'), max_length=155, unique=True, allow_unicode=True)
    description = models.TextField(_('توضیح محصول'), blank=True, null=True)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, related_name='product_images')
    is_active = models.BooleanField(_('فعال'), default=True)
    video = models.ForeignKey('videos.Movies', on_delete=models.PROTECT, related_name='product_videos', blank=True, null=True)
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, related_name='product_categories')

    objects = ActiveManager()

    def __str__(self) -> str:
        return self.en_name
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'products'


class Option(Create, Update):
    option_name = models.CharField(_('آپشن'), max_length=155)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_option')
    is_active = models.BooleanField(_('فعال'), default=True)

    objects = ActiveManager()

    def __str__(self) -> str:
        return self.option_name
    
    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')
        db_table = 'options'


class OptionValue(Create, Update):
    option = models.ForeignKey(Option, on_delete=models.PROTECT, related_name='option_values')
    option_value = models.CharField(_('نام آپشن'), max_length=155)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_option_value')
    is_active = models.BooleanField(_('فعال'), default=True)

    objects = ActiveManager()

    def __str__(self) -> str:
        return self.option_value
    
    class Meta:
        verbose_name = _('option value')
        verbose_name_plural = _('option values')
        db_table = 'option_values'


class Attribute(Create, Update):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_attribute')
    attribute_name = models.CharField(_('ویژگی'), max_length=155)
    is_active = models.BooleanField(_('فعال'), default=True)

    objects = ActiveManager()

    def __str__(self) -> str:
        return self.attribute_name
    
    class Meta:
        verbose_name = _('attribute')
        verbose_name_plural = _('attributes')
        db_table = 'attributes'


class AttributeValue(Create, Update):
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name='attribute_values')
    attribute_value = models.CharField(_('نام ویژگی'), max_length=155)
    attribute_text = models.TextField(_('توضیح ویژگی'), blank=True, null=True)
    attribute_date = models.DateField(_('تاریخ ویژگی'), blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_attribute_value')
    is_active = models.BooleanField(_('فعال'), default=True)

    objects = ActiveManager()

    def __str__(self) -> str:
        return self.attribute_value
    
    class Meta:
        verbose_name = _('attribute value')
        verbose_name_plural = _('attribute values')
        db_table = 'attribute_values'
