from django.urls import path
from . import views

urlpatterns = [
    path('searchSong/', views.search_song),
    path('filterSongByYear/', views.filter_songs_year),
    path('getAllSongs/', views.get_all_songs),
    path('addSong/', views.add_song),
    path('updateSong/', views.update_song),
    path('removeSong/<int:song_id>/', views.remove_song, name='remove_song'),
    path('getSong/<int:song_id>/', views.get_song, name='get_song'),
    path('searchSongClass/<str:song_name>/', views.SearchSongByName.as_view(), name='search_song_class'),
    path('songsClass/', views.ListSongs.as_view(), name='songs_class'),
    path('addSongFBV/', views.add_song),
    path('removeSongFBV/<int:song_id>/', views.remove_song),
]