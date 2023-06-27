from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', MusicHome.as_view(), name='home'),
    path('addplaylist/', AddPlaylist.as_view(), name='addplaylist'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('addalbumuser/<int:id>/', add_album_user, name='addalbum'),
    path('deletealbumuser/<int:id>/', delete_album_user, name='deletealbum'),
    path('addgroupuser/<int:id>/', add_group_user, name='addgroup'),
    path('deletegroupuser/<int:id>/', delete_group_user, name='deletegroup'),
    path('addtrackuser/<int:id>/', add_track_user, name='addtrack'),
    path('deletetrackuser/<int:id>/', delete_track_user, name='deletetrack'),
    path('addtrackplaylist/<int:id_playlist>/<int:id_track>/', add_track_playlist, name='addtrackplaylist'),
    path('deletetrackplaylist/<int:id_playlist>/<int:id_track>/', delete_track_playlist, name='deletetrackplaylists'),
    path('deleteplaylist/<int:id_playlist>/', delete_playlist, name='deleteplaylist'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('album/<slug:album_slug>/', ShowAlbum.as_view(), name='album'),
    path('groups/', MusicGroup.as_view(), name='groups'),
    path('groups/group/<slug:group_slug>/', ShowGroup.as_view(), name='group'),
    path('tracks/', MusicTrack.as_view(), name='tracks'),
    path('addtracks/<int:playlist_id>', MusicTrackPlaylist.as_view(), name='tracksplaylist'),
    path('genre/<slug:genre_slug>/', MusicGenre.as_view(), name='genre'),
    path('recs/', MusicRecomendationAlbum.as_view(), name='recs'),
    path('pred/', upload_file, name='pred'),
    path('predresult/', PredResult.as_view(), name='predresult'),
    path('track/<slug:track_slug>/', ShowTrack.as_view(), name='track'),
    path('profile/', ProfileView.as_view(), name='prof'),
    path('myplaylists/', PlaylistView.as_view(), name='myplaylists'),
    path('playlist/<int:pk>/', ShowPlaylist.as_view(), name='playlist'),
    path('pdf/<int:id_album>/', pdfview, name='pdfview'),
    path('pdfgroup/<int:id_group>/', pdfview_group, name='pdfviewgroup'),
]