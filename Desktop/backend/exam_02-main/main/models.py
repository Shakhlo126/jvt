from django.db import models
from packaging.tags import Tag


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=222)
    author = models.CharField(max_length=222, blank=True)
    tags = models.ManyToManyField('tag')
    price = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

class Category(models.Model):
    title = models.CharField(max_length=222)
    description = models.TextField()
    image = models.ImageField(upload_to='category_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

