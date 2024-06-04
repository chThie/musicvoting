import uuid
from django.db import models


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interpret = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    played = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.song_title} - {self.interpret} (Votes: {self.votes})"
