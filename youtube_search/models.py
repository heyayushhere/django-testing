

# Create your models here.
from django.db import models

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

