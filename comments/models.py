from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import ActiveComments
from core.models import Create, Update


class Comments(Create, Update):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='comment_user')
    title = models.CharField(_('عنوان نظر'), max_length=100)
    text = models.TextField(_('نظر'))
    is_active = models.BooleanField(_('فعال'), default=False)
    
    objects = ActiveComments()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('نظرات')
        verbose_name_plural = _('نظرات')
        db_table = 'comments'


class Rate(Create, Update):
    comment = models.ForeignKey(Comments, on_delete=models.PROTECT, related_name='rate_comment')
    score = models.PositiveSmallIntegerField(_('نمره'), blank=True, null=True)

    objects = ActiveComments()

    def __str__(self) -> str:
        return f'{self.comment.title} -- {self.score}'
    
    class Meta:
        verbose_name = _('نمره')
        verbose_name_plural = _('نمرها')
        db_table = 'rate'


class Questions(Create, Update):
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='question_user')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='question_product')
    text = models.TextField(_('متن سوال'))
    is_active = models.BooleanField(_('فعال'), default=False)

    objects = ActiveComments()

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = _('سوال')
        verbose_name_plural = _('سوالات')
        db_table = 'questions'


class Answer(Create, Update):
    question = models.ForeignKey(Questions, on_delete=models.PROTECT, related_name='answer_question')
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='answer_user')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='answer_product')
    text = models.TextField(_('پاسخ سوال'))
    is_active = models.BooleanField(_('فعال'), default=False)

    objects = ActiveComments()

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = _('پاسخ')
        verbose_name_plural = _('پاسخ ها')
        db_table = 'answer'
