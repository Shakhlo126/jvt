from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('travel_posts/<int:pk>/', DetailAPIView.as_view(), name='detail'),
    path('travel_posts/', Travel_postAPIView.as_view(), name='posts'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('popular/', Popular_articlesAPIView.as_view(), name='popular articles'),
]