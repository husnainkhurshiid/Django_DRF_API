from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def BookList(request, format=None):
    if request.method == 'GET':
        Bookdata = Book.objects.all()
        serializer = BookSerializer(Bookdata, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def BookDetail(request, id, format=None):

    try:
        BookData = Book.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(BookData)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(BookData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        BookData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
