from django.contrib import messages
from django.db import models
from django.db.models.deletion import CASCADE
from login_app.models import *



class Message(models.Model):
    message = models.TextField(max_length=2000)
    posted_by = models.ForeignKey(User, related_name='messages', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    message = models.ForeignKey(Message, related_name='comments',on_delete=CASCADE)
    owner = models.ForeignKey(User, related_name='posted_by', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)