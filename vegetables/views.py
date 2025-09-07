from django.shortcuts import render, redirect
from .models import Recipes
# Create your views here.


def recipes(request):
    if request.method == 'POST':
        data = request.POST
        Recipes.objects.create(
            name = data.get('recipeName'),
            description = data.get('recipeDescription'), 
            recipe_image = request.FILES.get('recipeImage')
            )
        
    recipes = Recipes.objects.all()
    return render(request, 'vegetables/recipes.html', context={'recipes': recipes})


def delete_recipe(request, id):
    Recipes.objects.get(id=id).delete()
    return redirect('recipes')