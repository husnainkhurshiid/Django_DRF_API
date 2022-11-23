from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # book_id = serializers.CharField(max_length=100, null=False)
    # book_title = serializers.CharField(max_length=100, null=False)
    # author_name = serializers.CharField(max_length=100, null=False)
    class Meta:
        model = Book
        fields = ['id', 'book_id', 'book_title', 'author_name']
