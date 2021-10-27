from os import name
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class BlogPost(models.Model):

    image = models.FileField(upload_to='post_pic/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:15]

class Comment(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post}: {self.text}"