from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Users, Job


class jobInline(admin.StackedInline):
    model = Job
    extra = 0

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'create_at', 'update_at')
    list_display = ('job_name', 'is_active')
    list_per_page = 20
    raw_id_fields = ('user',)
    list_editable = ('is_active',)


@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    inlines = (jobInline,)
    fieldsets = (
        (None, {"fields": ("mobile_phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "create_at", "update_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile_phone", "password1", "password2"),
            },
        ),
    )
    list_display = ("mobile_phone", "email", "first_name", "last_name", "is_staff", 'is_active', 'is_superuser')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("mobile_phone", "first_name", "last_name", "email")
    ordering = ("mobile_phone",)
    readonly_fields = ('create_at', 'update_at')