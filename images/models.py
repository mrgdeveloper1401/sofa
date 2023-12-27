from django.db import models
from django.utils.translation import gettext_lazy as _
from hashlib import sha1
from .exception import Deupicated
from core.models import Create, Update


class Images(Create, Update):
    image = models.ImageField(_('عکس'), width_field='width', height_field='height', upload_to='products/images/%Y/%m/%d')
    image_hash = models.CharField(_('هش'), max_length=40, unique=True, blank=True, null=True)
    image_size = models.PositiveIntegerField(_('حجم عکس'), default=0)
    alter_image = models.CharField(_('متن عکس'), max_length=100, blank=True, null=True)
    width = models.PositiveIntegerField(_('عرض'), default=0)
    height = models.PositiveIntegerField(_('ارتفاع'), default=0)
    focal_point_x = models.PositiveIntegerField(blank=True, null=True)
    focal_point_y = models.PositiveIntegerField(blank=True , null=True)
    focal_point_width = models.PositiveIntegerField(blank=True, null=True)
    focal_point_height = models.PositiveIntegerField(blank=True , null=True)

    def images_hash(self):
        hasher = sha1()
        for chunk in self.image.chunks():
            hasher.update(chunk)
        return hasher.hexdigest()
        
    def save(self):
        self.image_size = self.image.size
        self.image_hash = self.images_hash()
        if Images.objects.filter(image_hash=self.image_hash).exists():
            raise Deupicated('Image is elready exists')
        return super().save()
    
    class Meta:
        db_table = 'images'