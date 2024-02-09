from rest_framework import generics, viewsets
from .models import (Category,
                     Comment,
                     Travel_post,
                     Author,
                     About,
                     Tag)

from .serializers import (AuthorSerializer,
                          AboutSerializer,
                          CategorySerializer,
                          CommentSerializer,
                          Travel_post_serializer,
                          TagSerializer)


class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Travel_postAPIView(generics.ListAPIView):
    queryset = Travel_post.objects.all()
    serializer_class = Travel_post_serializer


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class HomeAPIView(generics.ListAPIView):
    queryset = Travel_post.objects.all()[:9]
    serializer_class = Travel_post_serializer


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Travel_post.objects.all()
    serializer_class = Travel_post_serializer

class Popular_articlesAPIView(generics.ListAPIView):
    queryset =Travel_post.objects.all()[:3]
    serializer_class = Travel_post_serializer
