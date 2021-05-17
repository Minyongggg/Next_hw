from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)
    date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    date_str = models.CharField(max_length=200, default=None)
    dday = models.DecimalField(max_digits=5, decimal_places=0, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default=None)

    def __str__(self):
        result = f"{self.post}: {self.content[:5]}"

        return result