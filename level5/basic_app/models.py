from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(User)
    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profilepic',blank=True)
    def __str__(self):
        return self.user.username
