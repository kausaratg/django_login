from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

users = User()
# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(users, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
