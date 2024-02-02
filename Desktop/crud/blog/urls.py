from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('get/', get, name='Get'),
    path('delete/', delete_post, name='Delete'),
    path('create/', create, name='Create'),
    path('update/', update, name='Update')
]
