from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CospBlog (models.Model):
    post_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    your_post = models.TextField()

    def __str__(self):
        return self.post_title + '\n' + str(self.author)
