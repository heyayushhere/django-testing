from django.contrib import admin

# Register your models here.
from .models import Video

from .models import FavoriteVideo
from django.contrib import admin
from .models import Playlist,Task

admin.site.register(Playlist)
admin.site.register(Task)


admin.site.register(Video)

admin.site.register(FavoriteVideo)