from django.db import models
from appy.models import User

# Create your models here.

class Message(models.Model):
    desc = models.TextField()
    author = models.ForeignKey(User, related_name = "messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #comments

class Comment(models.Model):
    desc = models.TextField()
    author = models.ForeignKey(User, related_name = "comments", on_delete = models.CASCADE)
    messages = models.ForeignKey(Message, related_name = "messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)