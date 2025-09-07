from django.db import models

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + str(self.view_count)