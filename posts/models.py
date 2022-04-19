from django.conf import settings
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=50)
  body = models.TextField()
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
