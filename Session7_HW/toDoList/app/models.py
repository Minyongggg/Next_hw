from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    date_str = models.CharField(max_length=200)
    dday = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.title
