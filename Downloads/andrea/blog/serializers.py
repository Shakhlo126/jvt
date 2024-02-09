from rest_framework import serializers
from .models import (Author,
                     About,
                     Category,
                     Comment,
                     Travel_post,
                     Tag)


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
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Travel_post_serializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Travel_post
        fields = ['id', 'title', 'image', 'tags', 'author', 'category', 'description', 'comment_set', 'created_at',
                  'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

