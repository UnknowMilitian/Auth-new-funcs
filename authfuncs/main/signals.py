from django.dispatch import receiver
from django.db.models.signals import post_init, post_save
from django.contrib.auth.models import User as DjangoUser

from .models import User, UserProfile


@receiver(post_save, sender=User)
def user_post_save(instance, sender, created, **kwargs):
    print(instance, sender, created, **kwargs)
