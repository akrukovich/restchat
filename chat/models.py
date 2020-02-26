from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now, db_index=True)
    author = models.TextField(max_length=50)
    email = models.EmailField()

    class Meta:
        ordering = ['-date_posted']

    def save(self, *args, **kwargs):

        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return self.content
