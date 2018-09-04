from django.contrib import admin

from .models import Event, Audio, Video, About, Contact, Gallery


# @admin.register(Gallery)
# class MyPicsAdmin(admin.ModelAdmin):
#     form = FileFieldForm


admin.site.register(Event)

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'venue', 'poster']
    fieldsets = (
        (None, {
            'fields': (
                ('poster', 'name', 'start', 'end', 'venue'))}),
        ('Slug', {
            'classes': ('hidden','collapse-toggle'),
            'fields': ('slug',),
        }))
    prepopulated_fields = {'slug': ('name', 'start')}


@admin.register(Audio)
class MixTapeAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded', 'description']
    fieldsets = (
        (None, {
            'fields': (
                ('poster', 'title', 'description', 'file'))}),
        ('Slug', {
            'classes': ('hidden', 'collapse-toggle'),
            'fields': ('slug',),
        }))
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Video, MixTapeAdmin)
admin.site.register(About)
admin.site.register(Contact)