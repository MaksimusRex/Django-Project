from django.db.models.signals import post_save
from django.dispatch import receiver

from theProject2.users.forms import AppUser
from theProject2.users.models import Profile


@receiver(post_save, sender=AppUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AppUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()