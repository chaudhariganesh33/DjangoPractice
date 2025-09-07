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

    if request.GET.get('search'):
        search_term = request.GET.get('search')
        print(search_term)
        recipes = Recipes.objects.filter(name__icontains=search_term)
        print(recipes)

    return render(request, 'vegetables/recipes.html', context={'recipes': recipes})


def delete_recipe(request, id):
    Recipes.objects.get(id=id).delete()
    return redirect('recipes')

def update_recipe(request, id):
    recipe = Recipes.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        recipe.name = data.get('recipeName')
        recipe.description = data.get('recipeDescription')
        recipe.recipe_image = request.FILES.get('recipeImage')
        recipe.save()
        return redirect('recipes')
    return render(request, 'vegetables/update_recipe.html', context={'recipe': recipe})