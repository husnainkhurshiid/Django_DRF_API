from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_id', 'book_title', 'author_name']
