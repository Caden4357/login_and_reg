from django.contrib import messages
from django.db import models
from django.db.models.deletion import CASCADE
from login_app.models import *

class Message(models.Model):
    message = models.TextField(max_length=2000)
    user = models.OneToOneField(User, related_name='message_owner', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    message = models.OneToOneField(Message, related_name='message_commited_on', on_delete=CASCADE)
    user = models.OneToOneField(User, related_name='user_comment', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)