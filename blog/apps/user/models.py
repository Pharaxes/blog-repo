from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


#genera nombre unico para el avatar del usuario usando su uuid
def get_avatar_filename(instance, filename):
    # Generar un nombre unico para el avatar usando el UUID del usuario
    # asdasdasdasdasdas.png
    _, file_extension = os.path.splitext(filename)
    new_filename = f"user-{instance.id}-avatar{file_extension}"
    # user\avatar\user-c9b6af13-94b3-412f-a2d1-0bc7ebc06594-avatar.png
    return os.path.join("user/avatar/", new_filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default=settings.AVATAR_DEFAULT_IMAGE
    )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url

    """Puede crear, editar y eliminar sus propios comentarios"""
    @property
    def is_registered(self):
        return self.groups.filter(name="registered").exists()

    """Puede crear y editar sus propios post"""
    """Puede crear, editar y eliminar sus propios comentarios"""
    """Puede eliminar los comentarios de otros usuarios en sus propios post"""
    @property
    def is_collaborator(self):
        return self.groups.filter(name="collaborator").exists()

    @property
    def is_moderator(self):
        return self.groups.filter(name="moderator").exists()