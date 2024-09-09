from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(_("Phone number"), max_length=15, unique=True)
    date_of_birth = models.DateField(_("Date of birth"))
    bio = models.CharField(_("Bio"), max_length=500)

    # Добавляем related_name для устранения конфликтов
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_user_set",  # Уникальное имя для обратной связи
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_user_permissions_set",  # Уникальное имя для обратной связи
    )

    def __str__(self):
        return self.phone_number


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        related_name="user",
        on_delete=models.CASCADE,
    )
    location = models.CharField(_("Location"), max_length=255, null=True)
    avatar = models.ImageField(_("Avatar"), upload_to="user-avatar", null=True)

    def __str__(self):
        return self.location
