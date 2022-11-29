from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    cooking_time = models.IntegerField(default=0)
    link = models.URLField(max_length=250, blank=True)
    instructions = models.TextField(blank=True)