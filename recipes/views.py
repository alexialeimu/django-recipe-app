from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def index(request):
	all_recipes = Recipe.objects.all()
	context = {'all_recipes': all_recipes}
	return render(request, 'recipes/index.html', context)