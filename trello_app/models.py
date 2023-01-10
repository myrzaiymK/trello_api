import datetime
# from datetime import datetime as dt
from django.db.models.functions import datetime as dt

from users.models import CustomUser as User
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Board(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    archive = models.BooleanField(default=False)
    # archive = models.ManyToManyField(User, related_name="archive", blank=True)

    def __str__(self):
        return self.title


class Column(models.Model):
    title = models.CharField(max_length=30, blank=True)
    board = models.ForeignKey('Board', related_name='column', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    board = models.ForeignKey('Board', related_name='card', on_delete=models.CASCADE)
    column = models.ForeignKey('Column', related_name='card', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    deadline = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, blank=True, related_name='member')
    member = models.CharField(max_length=30, blank=True)



class Label(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=30)
    color = models.ForeignKey('LabelColor', on_delete=models.CASCADE)


class LabelColor(models.Model):
    color = models.CharField(max_length=300)


class LabelCard(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, blank=True)
    label = models.ForeignKey('Label', on_delete=models.CASCADE, blank=True)


class CheckList(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=30)


class CheckListCard(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, blank=True)
    checklist = models.ForeignKey('CheckList', on_delete=models.CASCADE, blank=True)


class Attachment(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE, blank=True)
    file = models.FileField(null=True, blank=True)


class AttachmentCard(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, blank=True)
    attachment = models.ForeignKey('Attachment', on_delete=models.CASCADE, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(blank=True, max_length=30)
    body = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey('Card', blank=True, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.card)


class Favourites(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='favorite')
    board = models.ForeignKey('Board', on_delete=models.CASCADE, blank=True, related_name='favorite')

class RecentViews(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE, blank=True, related_name='recent_views')
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='recent_views')
    views_time = models.DateTimeField(auto_now=True)


