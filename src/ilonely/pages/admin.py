from django.contrib import admin
from pages.models import Profile, Post, Comment, Follow, Block, Thread, Message, Event

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Block)
admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Event)