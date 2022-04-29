from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainpage')


class CospBlog (models.Model):
    post_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    your_post = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    like = models.ManyToManyField(User, related_name='blog_posts')
    favourite = models.ManyToManyField(User,related_name='favourite', blank=True)
    category = models.CharField(max_length=100, default = 'None')


    def get_absolute_url(self):
        return reverse('postarticle', args=[str(self.id)])

    def total_likes(self):
        return self.like.count()