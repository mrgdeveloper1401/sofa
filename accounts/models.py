from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.mail import send_mail
from core.models import Create, Update
from .manaers import UserManagers, ActiveModel


class Users(AbstractBaseUser, PermissionsMixin, Create, Update):
    first_name = models.CharField(_('نام'), max_length=150)
    last_name = models.CharField(_('نام خانوادگی'), max_length=150)
    email = models.EmailField(_('ایمیل'), unique=True, blank=True, null=True)
    mobile_phone = models.CharField(_('شماره موبایل'), max_length=11, unique=True, db_index=True)
    is_active = models.BooleanField(_('فعال'), default=False)
    is_staff = models.BooleanField(_('مدیر'), default=False)
    birth_day = models.DateField(_('تاریخ تولد'), blank=True, null=True)
    image = models.ForeignKey('images.Images', on_delete=models.PROTECT, null=True, blank=True, related_name='user_image')
    
    objects = UserManagers()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "mobile_phone"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)



class Job(Create, Update):
    job_name = models.CharField(_('نام شغل'), unique=True, max_length=100)
    job_description = models.TextField(_('توضیحات شغل'), blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='job_user')
    is_active = models.BooleanField(_('فعال'), default=True)
    
    # objects = ActiveModel()
    
    def __str__(self) -> str:
        return self.job_name
    
    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'