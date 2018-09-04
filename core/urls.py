from django.urls.conf import path
from django.urls import include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/<slug>', views.EventDetail.as_view(), name='event-details'),
    path('events/', views.EventList.as_view(), name='events'),
    path('audio-mixes/', views.AudioList.as_view(), name='audio-mixes'),
    path('video-mixes/', views.VideoList.as_view(), name='video-mixes'),
    path('bio/', views.about, name='bio'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.MyPicsList.as_view(), name='gallery'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('dashboard/', views.admin, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
]
