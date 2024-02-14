from rest_framework import serializers
from .models import (Category,
                     Subscribe,
                     Post,
                     Insta_images,
                     Author,
                     Advertise,
                     Tag,
                     Comments
                     )

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'tags', 'author', 'category', 'description', 'created_at',
                  'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Insta_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insta_images
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
