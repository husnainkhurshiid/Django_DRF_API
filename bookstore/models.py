from django.db import models

# Create your models here.


class Book(models.Model):
    book_id = models.CharField(max_length=100, null=False)
    book_title = models.CharField(max_length=100, null=False)
    author_name = models.CharField(max_length=100, null=False)
