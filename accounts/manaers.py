from django.contrib.auth.models import BaseUserManager, UserManager


class UserManagers(BaseUserManager):
    def create_user(self, mobile_phone, password=None):
        if not mobile_phone:
            raise ValueError('user must be a mobile phone')
        user = self.model(mobile_phone=mobile_phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, mobile_phone, email, password=None):
        if not email:
            raise ValueError('superuser must be a email')
        email = self.normalize_email(email)
        user = self.create_user(mobile_phone=mobile_phone, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user