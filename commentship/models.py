from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    sentiment = models.CharField(max_length=200, blank=True, null=True)