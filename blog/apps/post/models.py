from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.db import models
import uuid
import os


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=150, blank=True)
    content = models.TextField(max_length=10000)
    allow_comments = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='posts')

    def __str__(self):
        return self.title

    @property
    def comments_count(self):
        return self.comments.count()

    def generate_unique_slug(self):
        """Generar un slug unico basado en el titulo"""
        slug = slugify(self.title)

        unique_slug = slug
        count = 1

        """la vida como programador"""
        """la-vida-como-programador-1"""
        """la-vida-como-programador-2"""
        """la-vida-como-programador-3"""
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{count}"
            count += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()

        super().save(*args, **kwargs)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content


def get_image_filename(instance, filename):
    post_id = instance.post.id
    images_count = instance.post.images.count()

    _, file_extension = os.path.splitext(filename)
    new_filename = f"post-{post_id}-image-{images_count + 1}{file_extension}"

    # post/cover/post-c9b6af13-94b3-412f-a2d1-0bc7ebc06594-image-1.png
    # post/cover/post-c9b6af13-94b3-412f-a2d1-0bc7ebc06594-image-2.png
    # post/cover/post-c9b6af13-94b3-412f-a2d1-0bc7ebc06594-image-3.png
    return os.path.join("post/cover/", new_filename)


class PostImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(
        upload_to=get_image_filename, default=settings.POST_DEFAULT_IMAGE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"{self.id}"