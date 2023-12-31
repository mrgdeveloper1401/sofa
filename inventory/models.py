from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update


class Stock(Create, Update):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='stockrecords')
    sku = models.CharField(_('شناسه انحصاری کالا'), max_length=64, null=True, blank=True, unique=True)
    buy_price = models.PositiveBigIntegerField(_('قیمت خرید'), null=True, blank=True)
    sale_price = models.PositiveBigIntegerField(_('قیمت فروش'))
    num_stock = models.PositiveIntegerField(_('تعداد کالا'), default=0)
    threshold_low_stack = models.PositiveIntegerField(_('حد نصاب پایین کالا'), null=True, blank=True)    
    is_active = models.BooleanField(_("فعال"), default=True)
    
    def __str__(self) -> str:
        return self.sku
    
    class Meta:
        db_table ='stocks'
        verbose_name ='stock'
        verbose_name_plural ='stocks'
