from django.contrib import admin
from django.urls import path, include
from youtube_search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('search/', views.search_videos, name='search_videos'),
    path('favorite-video/', views.favorite_video, name='favorite_video'),
]
