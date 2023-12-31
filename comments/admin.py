from django.contrib import admin
from .models import Comments, Questions, Answer


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', 'user', )
    list_display = ('title', 'product', 'user', 'create_at', 'update_at', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('product', 'user', 'title')
    list_filter = ('create_at', 'update_at', 'is_active')
    list_per_page = 20


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'product')
    list_display = ('user', 'product', 'text', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active','create_at', 'update_at')
    list_per_page = 20
    search_fields = ('user', 'product', 'text')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    raw_id_fields = ('question', 'user', 'product')
    list_display = ('question', 'user', 'product', 'text', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active','create_at', 'update_at')
    search_fields = ('question', 'user', 'product', 'text')
    list_per_page = 20
