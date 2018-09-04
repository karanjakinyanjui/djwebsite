from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import PhotoForm
from .models import Event, Audio, Video, MixTape, About, MyPics


class EventList(ListView):
    model = Event


class AudioList(ListView):
    model = Audio


class VideoList(ListView):
    model = Video
    template_name = 'core/audio_list.html'


class AudioDetail(DetailView):
    model = Audio


class EventDetail(DetailView):
    model = Event


def about(request):
    bio = About.objects.get(id=1)
    return render(request,
                  'core/about.html',
                  context={
                      'bio': bio
                  })


def home(request):
    mixes = MixTape.objects.all()[:8]
    events = Event.objects.all()[:4]

    return render(request,
                  'core/home.html',
                  context={
                      'mixes': mixes,
                      'events': events,
                  })


def contact(request):
    return render(request,
                  'core/contact.html',
                  context={})


def admin(request):
    audio = Audio.objects.count()
    video = Video.objects.count()
    pics = MyPics.objects.count()
    events = Event.objects.count()

    return render(request,
                  'core/admin.html',
                  context={
                      'audio': audio,
                      'video': video,
                      'pics': pics,
                      'events': events,
                  })


class MyPicsList(ListView):
    model = MyPics


# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'core/upload.html'  # Replace with your template.
#     success_url = '/home/'  # reverse('core:gallery')
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         print(form.errors)
#         files = request.FILES.getlist('pics')
#         print(request.FILES)
#         if form.is_valid():
#             print('form_valid')
#             for f in files:
#                 pic = MyPics.objects.create(picture=f)
#                 pic.save()
#             return self.form_valid(form)
#         else:
#             print('form is invalid')
#             return self.form_invalid(form)


class UploadView(View, LoginRequiredMixin):
    def get(self, request):
        photos_list = MyPics.objects.all()
        return render(self.request, 'core/upload.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
