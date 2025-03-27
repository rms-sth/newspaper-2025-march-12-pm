from django.contrib import admin
from newspaper.models import Category, Comment, Contact, Tag, Post, UserProfile
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Contact)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)
