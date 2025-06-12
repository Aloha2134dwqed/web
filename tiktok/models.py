from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ContentType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TikTokContent(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    followers_gained = models.PositiveIntegerField(default=0)
    date_posted = models.DateField(default=timezone.now)
    is_trending = models.BooleanField(default=False)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"