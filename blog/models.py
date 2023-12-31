from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from .managers import ActiveManager


class Post(Create, Update):
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='user_post')




class Job(Create, Update):
    job_name = models.CharField(_('نام شغل'), unique=True, max_length=100)
    job_description = models.TextField(_('توضیحات شغل'), blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='job_post')
    is_active = models.BooleanField(_('فعال'), default=True)
    
    objects = ActiveManager()
    
    def __str__(self) -> str:
        return self.job_name
    
    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class PostTitle(Create, Update):
    title = models.CharField(_("عنوان"), max_length=255, db_index=True)
    slug = models.SlugField(_('اسلاگ'), max_length=255, allow_unicode=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_title_post')
    
    objects = ActiveManager()

    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        db_table = 'post_title'
        verbose_name = 'Post Title'
        verbose_name_plural = 'Post Titles'


class PostDescription(Create, Update):
    description = models.TextField(_('توضیحات'), blank=True, null=True)
    is_active = models.BooleanField(_("فعال"), default=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_description')
    
    objects = ActiveManager()

    def __str__(self) -> str:
        return self.description
    
    
    class Meta:
        db_table = 'post_description'
        verbose_name = 'Post Description'
        verbose_name_plural = 'Post Descriptions'


class PostImage(Create, Update):
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, related_name='image_post')
    is_active = models.BooleanField(_('فعال'), default=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_image')
    
    objects = ActiveManager()

    class Meta:
        db_table = 'post_image'
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post Images'


class CommentPost(Create, Update):
    title = models.CharField(_("عنوان"), max_length=255)
    description = models.TextField(_('توضیح'))
    is_active = models.BooleanField(_('فعال'), default=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comment_post')
    
    class Rate(models.TextChoices):
        one = '1', _('1')
        two = '2', _('2')
        three = '3', _('3')
        four = '4', _('4')
        five = '5', _('5')
    rate_choose = models.CharField(_('امتیاز'), max_length=5, choices=Rate.choices, default=Rate.five)

    objects = ActiveManager()

    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        db_table = 'comment_post'
        verbose_name = 'Comment Post'
        verbose_name_plural = 'Comment Posts'