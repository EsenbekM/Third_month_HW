from django.db import models

# Create your models here.

class BlogPost(models.Model):

    image = models.FileField(upload_to='post_pic/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title[:15]
    
    def get_absolute_url(self):
        return f"/blog/{self.pk}/"


class Comment(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post}: {self.text}"