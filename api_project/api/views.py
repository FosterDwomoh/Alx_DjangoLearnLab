from rest_framework import generics
from .models import Bookfrom .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(Viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

