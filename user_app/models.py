from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,11}$',
                                 message="Phone number must be entered in the format: '+99 999 999 999'. "
                                         "Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    avatar = models.ImageField(upload_to='profile_images/', blank=True)


class UserTier(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tier')

    def __str__(self):
        return self.name
