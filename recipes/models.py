from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    cooking_time = models.IntegerField(default=0)
    link = models.URLField(max_length=250, blank=True)
    image = models.ImageField(upload_to='recipes', blank=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name