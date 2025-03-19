from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Don't create table in DB


class Category(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# category.post_set.count()
class Post(TimeStampModel): # post.tag.all
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count = models.PositiveBigIntegerField(default=0)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


# user - post relationship
# 1 user can have multiple posts => M
# 1 post can be associated only 1 user => 1
# ForeignKey => Many => Post

# Category - Post Relationship
# 1 category can have M posts => M
# 1 post can be associated to 1 category => 1
# ForeignKey => Many => Post


# Tag - Post Relationship
# 1 tag can be associated to M posts => M
# 1 post can have M tags => M
# ManyToManyField => any model


# 1 category can have multiple products => M
# 1 product can be associated to M category => M
# ManyToManyField => any model