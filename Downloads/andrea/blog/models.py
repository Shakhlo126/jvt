from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='auhtors')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Travel_post(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='posts')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Travel_post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='posts')
    description = models.TextField()title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)