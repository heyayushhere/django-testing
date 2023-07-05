

# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class FavoriteVideo(models.Model):
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.video_id


class Playlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return self.user.username + "'s Playlist"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



