from django.db import models
from django.utils.translation import gettext_lazy as _


class Create(models.Model):
    create_at = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True, editable=False)
    
    class Meta:
        abstract = True


class Update(models.Model):
    update_at = models.DateTimeField(_('تاریخ ویرایش'), auto_now=True, editable=False)
    
    
    class Meta:
        abstract = True
