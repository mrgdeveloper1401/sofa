from django.contrib import admin
from .models import Comments, Questions, Rate, Answer


class RateInline(admin.TabularInline):
    model = Rate
    extra = 0


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    inlines = (RateInline, )


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
