from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import AddRecipeForm
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

def addRecipeView(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
            form = AddRecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})