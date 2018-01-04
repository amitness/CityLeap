from django.db import models


class Complain(models.Model):
    text = models.CharField(max_length=100)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    upvote_count = models.IntegerField(default=True, null=True)
    category = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
