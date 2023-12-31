from django.contrib import admin
from .models import Job, Post, PostTitle, PostDescription, PostImage, CommentPost


class jobInline(admin.TabularInline):
    model = Job
    extra = 0

class PostTitleInline(admin.TabularInline):
    model = PostTitle
    extra = 0


class PostDescriptionInline(admin.TabularInline):
    model = PostDescription
    extra = 0


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'create_at', 'update_at')
    list_display = ('job_name', 'is_active')
    list_per_page = 20
    raw_id_fields = ('post',)
    list_editable = ('is_active',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (jobInline, PostTitleInline, PostDescriptionInline, PostImageInline)
    raw_id_fields = ('user', )
    list_filter = ('create_at', 'update_at')
    

@admin.register(PostTitle)
class PostTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'post')
    prepopulated_fields = {'slug': ('title', )}
    list_editable = ('is_active',)
    list_filter = ('is_active', 'create_at', 'update_at')


@admin.register(PostDescription)
class PostDescriptionAdmin(admin.ModelAdmin):
    list_display = ('post', 'is_active', 'create_at', 'update_at')
    raw_id_fields = ('post', )
    list_editable = ('is_active',)
    list_filter = ('is_active', 'create_at', 'update_at')
    list_per_page = 20


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('image', 'post',)
    list_filter = ('is_active', 'create_at', 'update_at')
    list_display = ('image', 'post', 'is_active')
    list_per_page = 20
    list_editable = ('is_active',)


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    raw_id_fields = ('post',)
    list_display = ('title', 'rate_choose', 'is_active')
    list_filter = ('create_at', 'update_at', 'is_active')
    list_per_page = 20
    list_editable = ('is_active',)

