from django.db import models

# Create your models here.
from django.db import models


class EmailMessage(models.Model):
    content = models.TextField()
    is_spam = models.BooleanField()
