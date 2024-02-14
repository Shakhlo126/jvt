from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.TextField()
    author_name = models.CharField(max_length=212)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    description = models.TextField()
    quotes = models.TextField
    extra_images = models.ImageField(upload_to='posts')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    image = models.ImageField(upload_to='posts')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Insta_images(models.Model):
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

class Advertise(models.Model):
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='posts')
    description = models.TextField()
    profession = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=155)
    github_link = models.CharField(max_length=200)
    insta_link = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=202)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
