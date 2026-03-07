from django.contrib import admin
from .models import Univer, Faculty, FileWork


@admin.register(Univer)
class ModelUniver(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = list_display[1:]
    prepopulate_fields = {'slug': ('name')}
    search_fields = 'name', 'slug', 'faculties__name'


@admin.register(Faculty)
class ModelFaculty(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'univer')
    list_display_links = 'name',
    prepopulate_fields = {'slug': ('name')}
    search_fields = 'name', 'slug', 'univer__name'
    list_filter = 'univer__name',


@admin.register(FileWork)
class ModelFaculty(admin.ModelAdmin):
    list_display = ('id', 'theme', 'faculty', )
    list_display_links = 'theme',
    prepopulate_fields = {'slug': ('name')}
    search_fields = 'name', 'slug', 'univer__name', 'faculty__name'
    list_filter = 'faculty__name', 'faculty__univer__name'






