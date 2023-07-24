from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Statistics(models.Model):
    datetime = models.DateTimeField(default=datetime.now())

    player_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player_1")
    player_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player_2")

    score = models.IntegerField(default=0)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner")

    class Meta:
        unique_together = ("player_1", "player_2")
