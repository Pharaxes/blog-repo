from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

#genera nombre unico para el avatar del usuario usando su uuid
def get_avatar_filename(instance, filename):
    #asdadadadad.png
    _, file_extension = os.path.splitext(filename)
    new_filename = f"user-{instance.id}-avatar{file_extension}"
    #user/avatar/user-uuid-avatar.png
    return os.path.join("user/avatar/", new_filename)


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=30, unique=True, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default="user/default/avatar-default.png"
    )

    def __str__(self):
        return self.username
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url