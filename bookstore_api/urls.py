from django.contrib import admin
from django.urls import path
from bookstore import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookList),
    path('books/<int:id>', views.BookDetail),
]


urlpatterns = format_suffix_patterns(urlpatterns)
