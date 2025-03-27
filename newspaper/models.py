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
# category.post_set.all()

# post.author.userprofile.image.url
class Post(TimeStampModel):  # post.tag.all
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


class UserProfile(TimeStampModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_images/%Y/%m/%d", blank=False)
    address = models.CharField(max_length=200)
    biography = models.TextField()

    def __str__(self):
        return self.user.username


# post.comment_set.count
# post.comment_set.all


class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} | {self.comment[:70]}"


class Newsletter(TimeStampModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Contact(TimeStampModel):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


# comment - post
# 1 post can have M comments => M
# 1 comment can be associated to 1 post => 1
# ForeginKey => Many


# user - userprofile
# 1 user can have 1 profile => 1
# 1 profile can be associated to 1 user => 1
# OneToOneField => Any Model => UserProfile

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
