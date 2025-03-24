from django.contrib import admin
from newspaper.models import Category, Comment, Tag, Post, UserProfile

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
