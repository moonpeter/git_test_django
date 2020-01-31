from django.db import models


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('member.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
