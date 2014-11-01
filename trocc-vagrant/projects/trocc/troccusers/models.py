from django.db import models
from django.contrib.auth.models import AbstractUser, User

class TroccUser(AbstractUser):
    rating = models.PositiveSmallIntegerField(default=0)
    date_of_birth = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.username

