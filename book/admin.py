from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name_book', 'author','number_pages']
    list_filter = ['author']