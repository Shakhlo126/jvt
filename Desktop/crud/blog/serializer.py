from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = ['id', 'title' , 'content' , 'created_at' , 'updated_at']
        read_only_fields = ['created_at' , 'updated_at']