from django.db import models
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + str(self.view_count)
        

@receiver(signals.post_save, sender = Recipes)
def call_recipe_api(sender, instance, **kwargs):
    print("\nRecipe object created\n")