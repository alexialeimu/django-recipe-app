from django.contrib import admin
from .models import Recipe

class imageAdmin(admin.ModelAdmin):
    list_display = ["name", "image_title", "image"] # fix this

admin.site.register(Recipe, imageAdmin)