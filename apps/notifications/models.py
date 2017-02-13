from django.contrib.auth.models import User
from django.db import models


class FirebaseToken(models.Model):
    """
    It stores the firebase id with corresponding users.
    """
    user = models.ForeignKey(User)
    firebase_token = models.CharField(max_length=200, blank=False, null=False)


class Preferences(models.Model):
    """
    It stores the user Preferences with corresponding users.
    """
    user = models.OneToOneField(User)
    notification_preferences = models.CharField(max_length=200, blank=False, null=False, default='00000')
