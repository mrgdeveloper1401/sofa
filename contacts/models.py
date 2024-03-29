from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Update, Create
from .managers import ActiveModel


class ContactUs(Create, Update):
    title = models.CharField(_('موضوع پیام'), max_length=100)
    email = models.EmailField(_('ایمیل'), max_length=155)
    body = models.TextField(_('متن پیام'))
    
    # objects = ActiveModel()
    
    def __str__(self) -> str:
        return f'{self.title} - {self.email}'
    
    class Meta:
        db_table = 'contact_us'
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'


class AddressMe(Create, Update):
    place_name = models.TextField(_('مکان'))
    
    # objects = ActiveModel()
    
    def __str__(self) -> str:
        return self.place_name
    
    class Meta:
        db_table = 'address_me'
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان'
        

class CallMe(Create, Update):
    mobile_phone = models.CharField(_('شماره تلفن'), max_length=11)
    landing_phone = models.CharField(_('تلفن ثابت'), max_length=12)
    is_active = models.BooleanField(_('فعال'), default=True)
    address_me = models.ForeignKey(AddressMe, on_delete=models.PROTECT, related_name='address_me')
    
    # objects = ActiveModel()

    def __str__(self) -> str:
        return f'{self.mobile_phone} - {self.landing_phone}'
    
    class Meta:
        db_table = 'call_me'
        verbose_name = 'تلفن همراه'
        verbose_name_plural = 'تلفن همراه'


class Services(Create, Update):
    title = models.CharField(_('عنوان'), max_length=100)
    description = models.TextField(_('توضیحات'))
    is_active = models.BooleanField(_('فعال'), default=True)

    # objects = ActiveModel()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table ='services'
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'


class AboutUs(Create, Update):
    title = models.CharField(_('عنوان'), max_length=100)
    description = models.TextField(_('توضیحات'))
    is_active = models.BooleanField(_('فعال'), default=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table ='about_us'
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class Faq(Create, Update):
    question = models.CharField(_('سوال'), max_length=255)
    answer = models.TextField(_('توضیحات'))
    is_active = models.BooleanField(_("فعال"), default=True)
    
    def __str__(self) -> str:
        return self.question
    
    class Meta:
        db_table ='faq'
        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات متداول'