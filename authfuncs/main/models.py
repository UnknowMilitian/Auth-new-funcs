from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(_("Phone number"), max_length=15, unique=True)
    date_of_birth = models.DateField(_("Date of birth"))
    bio = models.CharField(_("Bio"), max_length=500)

    def __str__(self):
        return self.phone_number


class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), related_name="user_profile")
    location = models.CharField(_("Location"), max_length=255)
    avatar = models.ImageField(_("Avatar"), upload_to="user-avatar")

    def __str__(self):
        return self.location
