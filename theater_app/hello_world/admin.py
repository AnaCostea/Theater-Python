from django.contrib import admin

from hello_world.models import Author, Play, PlayInfo, Type, Actor

admin.site.register(Author)
admin.site.register(Play)
admin.site.register(PlayInfo)
admin.site.register(Type)
admin.site.register(Actor)
