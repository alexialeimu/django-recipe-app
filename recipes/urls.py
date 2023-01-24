from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
	path('', views.index, name='index'),
	path('recipes/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipes/add_recipe/', views.addRecipeView, name='add_recipe')
]