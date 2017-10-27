from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=255)

    def __str__(self):
        """Return a human readable version of a message."""
        return "{}".format(self.message_text)
