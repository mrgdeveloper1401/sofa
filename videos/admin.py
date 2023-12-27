from django.contrib import admin
from .models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    pass
