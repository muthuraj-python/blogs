from django.contrib import admin

from blogs.models import Blog, Entry, UserComment

admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(UserComment)

