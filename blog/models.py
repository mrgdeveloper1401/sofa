from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from .managers import ActiveManager


class Post(Create, Update):
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='user_post')
    title = models.CharField(_("عنوان پست"), max_length=255)
    slug = models.SlugField(_("اسلاگ"), max_length=255, unique=True, allow_unicode=True)
    description = models.TextField(_('توضیحات'))
    is_active = models.BooleanField(_('فعال'), default=True)
    
    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class CommentPost(Create, Update):
    title = models.CharField(_("عنوان"), max_length=255)
    description = models.TextField(_('توضیح'))
    is_active = models.BooleanField(_('فعال'), default=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comment_post')
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='user_comment_post')
    
    class Rate(models.TextChoices):
        one = '1', _('1')
        two = '2', _('2')
        three = '3', _('3')
        four = '4', _('4')
        five = '5', _('5')
    rate_choose = models.CharField(_('امتیاز'), max_length=5, choices=Rate.choices, default=Rate.five)

    # objects = ActiveManager()

    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        db_table = 'comment_post'
        verbose_name = 'Comment Post'
        verbose_name_plural = 'Comment Posts'