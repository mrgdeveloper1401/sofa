from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from core.models import Create, Update
from .managers import PublicCategory


class Category(Create, Update, MPTTModel):
    title = models.CharField(_('عنوان'), max_length=100, db_index=True)
    slug = models.SlugField(_('اسلاگ'), allow_unicode=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(_('فعال'), default=True)
    
    # objects = PublicCategory()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'category'


class Brand(Create, Update):
    brand_name = models.CharField(_('نام برند'), max_length=155, db_index=True, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='brand_categories')
    is_active = models.BooleanField(_('فعال'), default=True)
    
    def __str__(self) -> str:
        return f'{self.brand_name} {self.category}'
    
    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')
        db_table = 'brands'