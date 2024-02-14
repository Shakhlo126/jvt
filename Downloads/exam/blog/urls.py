from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('posts/<int:pk>/', DetailAPIView.as_view(), name='detail'),
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('insta_images/', Insta_imagesAPIView.as_view(), name='insta_images'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('advertise/', AdvertiseAPIView.as_view(), name='advertise'),
]