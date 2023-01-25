from django import forms
from .models import Recipe

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'instructions', 'cooking_time', 'link', 'image']