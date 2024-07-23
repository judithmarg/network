from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    n_followers = models.IntegerField(default=0)
    n_follows = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.username} tiene {self.n_followers} sigue {self.n_follows}'

    def increment_follow(self):
        self.n_follows += 1
        self.save()

    def decrement_follow(self):
        self.n_follows -= 1
        self.save()
        
class Post(models.Model):
    content = models.CharField(max_length=128)
    date = models.DateField(null=True, auto_now=True)
    time = models.TimeField(null=True, auto_now=True)
    username_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    n_likes = models.IntegerField(default=0)

    def __str__(self):
        return  f'{self.id}: {self.content} by {self.username_post}'
    
    def edit(self, new_content):
        self.content = new_content
        self.save()
    
class Follow(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_id")
    following_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_id")

    def __str__(self):
        return f'{self.id} donde {self.follower_id} sigue a {self.following_id}'

