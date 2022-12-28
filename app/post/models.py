from django.db import models
from account.models import User


class Post(models.Model):
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
