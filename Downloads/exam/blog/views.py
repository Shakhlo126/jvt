from rest_framework import generics, viewsets
from .models import (Category,
                     Subscribe,
                     Post,
                     Insta_images,
                     Author,
                     Advertise,
                     Tag,
                     Comments
                     )

from .serializers import (AuthorSerializer,
                          SubscribeSerializer,
                          CategorySerializer,
                          CommentSerializer,
                          Insta_imagesSerializer,
                          PostSerializer,
                          TagSerializer,
                          AdvertiseSerializer)


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
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SubscribeAPIView(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class Insta_imagesAPIView(generics.ListAPIView):
    queryset = Insta_images.objects.all()
    serializer_class = Insta_imagesSerializer


class AdvertiseAPIView(generics.ListAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseSerializer


class HomeAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:6]
    serializer_class = PostSerializer


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PopularpostsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:4]
    serializer_class = PostSerializer


