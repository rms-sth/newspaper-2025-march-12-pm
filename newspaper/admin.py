from django.contrib import admin
from newspaper.models import Category, Tag, Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
