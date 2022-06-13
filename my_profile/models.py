"""
Profile Models
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
GENDER_CHOICES = (
    ('female', 'Female'),
    ('male', 'Male'),
    ('other', 'Other'),
)


class UsersProfile(models.Model):
    """
    A User Profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class PetProfile(models.Model):
    """
    The Pet Profile Model
    """
    pet_owner = models.ForeignKey(UsersProfile, blank=False, null=False,
                                  on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=254, null=False, blank=False)
    breed = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default='other', null=False, blank=False)
    measurement_a = models.IntegerField(null=True, blank=True)
    measurement_b = models.IntegerField(null=True, blank=True)
    measurement_c = models.IntegerField(null=True, blank=True)
    pet_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.pet_name)


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):
    """
    Create/Update the User Profile
    """
    if created:
        UsersProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
