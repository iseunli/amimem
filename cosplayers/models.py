from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class CospBlog (models.Model):
    post_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    your_post = models.TextField()

    def get_absolute_url(self):
        return reverse('postarticle', args=[str(self.id)])