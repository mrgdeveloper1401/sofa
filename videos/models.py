from django.db import models
from hashlib import sha1
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from .exception import Deupicated


class Movies(Create, Update):
    movie = models.FileField(_('فیلم'), upload_to='products/movies/%Y/%m/%d')
    video_hash = models.CharField(_('هش ویدیو'), max_length=40, blank=True, null=True, unique=True)
    video_size = models.PositiveIntegerField(_('سایز ویدیو'), default=0, blank=True, null=True)
    caption_video = models.CharField(_('متن ویدیو'), max_length=100, blank=True, null=True)
    
    def videos_hasher(self):
        hasher = sha1()
        for chunk in self.movie.chunks():
            hasher.update(chunk)
        return hasher.hexdigest()
    
    def save(self):
        self.video_size = self.movie.size
        self.video_hash = self.videos_hasher()
        if Movies.objects.filter(video_hash=self.video_hash).exists():
            raise Deupicated('Movie is elready exists')
        return super().save()
    
    def __str__(self) -> str:
        return self.video_hash
    
    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
        db_table ='movies'

