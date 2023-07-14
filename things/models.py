from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Thing(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()

    def __str__(self):
        return self.title