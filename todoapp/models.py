
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text