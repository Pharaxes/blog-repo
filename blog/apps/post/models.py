from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import os

def get_image_filename(instance, filename):
    post_id = instance.post.id
    image_count = instance.post.images.count()
    _, file_extension = os.path.splitext(filename)
    new_filename = f"post-{post_id.id}-image-{image_count+1}"
    #user/avatar/post-uuid-image-1.png
    return os.path.join("post/cover/", new_filename)


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    allow_comments = models.BooleanField(default=True)
    avatar = models.ImageField(
        upload_to=get_image_filename, default="post/default/post-default.png"
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def ammount_comments(self):
        return self.comments.count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        
        super().save(*args, **kwargs)



    #def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
    #    return super().save(force_insert, force_update, using, update_fields)
    def generate_unique_slug(self):
        """Generar un slug unico usando el titulo"""
        slug = slugify(self.title)
        unique_slug = slug
        count = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{count}"
            count += 1
        
        return unique_slug


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content



class PostImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=get_image_filename, default="post/default/post-default")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.id