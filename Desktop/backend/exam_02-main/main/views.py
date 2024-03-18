from rest_framework import generics
from .serializers import TagSerializer, CategorySerializer, BookSerializer
from .models import Tag, Category,Book


class PostList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('category')
        if tag is not None:
            return Book.objects.filter(tags__title=tag)
        if category is not None:
            return Book.objects.filter(category__title=category)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
