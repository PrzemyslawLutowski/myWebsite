from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from main.models import DateTimeUpdate

class BlogPost(DateTimeUpdate):
    class Status(models.TextChoices):
        DRAFT = 'Draft', 'Roboczy'
        PUBLISHED = 'Published', 'Opublikowany'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, choices=Status, default=Status.DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')


    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
