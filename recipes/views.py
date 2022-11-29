from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Recipe

def index(request):
	all_recipes = Recipe.objects.all()
	context = {'all_recipes': all_recipes}
	return render(request, 'recipes/index.html', context)

def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'recipes/recipe.html', {'recipe': recipe})