from newspaper.models import Category, Post, Tag


def navigation(request):
    return {
        "categories": Category.objects.all()[:3],
        "tags": Tag.objects.all()[:12],
        "trending_posts": Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-views_count")[:3],
        "side_categories": Category.objects.all()[:6],
        "side_posts": Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:5],
    }
