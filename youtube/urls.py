from django.contrib import admin
from django.urls import path, include
from youtube_search import views
from django.urls import path
from youtube_search.views import add_to_playlist,my_playlist,task_list, create_task, update_task



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('search/', views.search_videos, name='search_videos'),
    path('favorite-video/', views.favorite_video, name='favorite_video'),                                       
    path('add-to-playlist/<video_id>/', add_to_playlist, name='add_to_playlist'),
    path('my-playlist/', my_playlist, name='my_playlist'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/update/<int:pk>/', update_task, name='update_task'),
]
