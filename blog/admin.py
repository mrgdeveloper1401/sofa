from django.contrib import admin
from .models import Post, CommentPost



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', )
    list_filter = ('create_at', 'update_at', 'is_active')
    list_display = ('title', 'user', 'is_active', 'id')
    search_fields = ('title',)
    list_editable = ('is_active',)
    list_per_page = 20
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'user')
    list_display = ('title', 'description', 'rate_choose', 'is_active', 'id')
    list_filter = ('create_at', 'update_at', 'is_active')
    list_per_page = 20
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
