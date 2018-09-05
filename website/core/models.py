from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel


class MixTape(PolymorphicModel):
    title = models.CharField('Title', max_length=140)
    poster = models.ImageField(upload_to='pics', null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500, null=True)
    uploaded = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-uploaded',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return


class Audio(MixTape):
    file = models.FileField(upload_to='audio', null=True)

    class Meta:
        verbose_name_plural = 'Audio'

class Video(MixTape):
    file = models.FileField(upload_to='video', null=True)

    class Meta:
        verbose_name_plural = 'Video'


class MyPics(models.Model):
    file = models.ImageField(upload_to='pics', null=True)
    uploaded = models.DateField(auto_now_add=True)

    def set_as_bio(self):
        About.objects.get(id=1).picture = self


class Gallery(models.Model):
    photo = models.ForeignKey(MyPics, related_name='photos', on_delete=models.DO_NOTHING)


class About(models.Model):
    picture = models.ImageField(upload_to='pics', null=True)
    about = models.TextField()


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    phone_2 = models.CharField(max_length=50)
    facebook = models.URLField(null=True, blank=True)
    beatport = models.URLField(null=True, blank=True)
    soundcloud = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)


class Event(models.Model):
    name = models.CharField('Event', max_length=140)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.CharField(max_length=140)
    slug = models.SlugField(max_length=50, unique=True)
    poster = models.ImageField(upload_to='pics', null=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-start',)

    def __str__(self):
        return f'{self.name} ({self.date.strftime("%b %d")})'

    @property
    def admin_slug(self):
        return f'{self.name}-{self.date.strftime("%b-%d")}'

    @property
    def date(self):
        return self.start.date()

    def get_absolute_url(self):
        return reverse('core:event-details', args=[self.slug])