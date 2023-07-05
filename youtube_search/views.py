from django.shortcuts import render, HttpResponse
from googleapiclient.discovery import build
from django.conf import settings
from .models import Video, FavoriteVideo,Playlist

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Task


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'youtube_search/registration/register.html', {'form': form})

def profile(request):
    return render(request, 'youtube_search/registration/profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Rest of the code for search_videos and favorite_video views...


def search_videos(request):
    videos = []
    if 'q' in request.GET:
        query = request.GET['q']

        youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
        response = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=15
        ).execute()

        
        for item in response['items']:
            video_id = item['id'].get('videoId')
            if video_id:
                video = Video(
                    title=item['snippet']['title'],
                    description=item['snippet']['description'],
                    video_id=video_id
                )
                videos.append(video)

        # Save videos to the database
        Video.objects.bulk_create(videos)

    return render(request, 'youtube_search/search.html', {'videos': videos})

def favorite_video(request):
    if request.method == 'POST':
        video_id = request.POST.get('video_id')

        # Check if the video is already in favorites
        if FavoriteVideo.objects.filter(video_id=video_id).exists():
            # Remove video from favorites
            FavoriteVideo.objects.filter(video_id=video_id).delete()
            is_favorite = False
        else:
            # Add video to favorites
            FavoriteVideo.objects.create(video_id=video_id)
            is_favorite = True

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

def add_to_playlist(request, video_id):
    playlist, created = Playlist.objects.get_or_create(user=request.user)
    video = Video.objects.get(video_id=video_id)
    playlist.videos.add(video)
    return redirect('my_playlist')



def my_playlist(request):
    playlist = Playlist.objects.filter(user=request.user).first()  # Retrieve the user's playlist
    context = {'playlist': playlist}
    return render(request, 'youtube_search/my_playlist.html', context)

from django.shortcuts import render, redirect
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'youtube_search/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'youtube_search/create_task.html', {'form': form})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'youtube_search/update_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('youtube_search/task_list')
