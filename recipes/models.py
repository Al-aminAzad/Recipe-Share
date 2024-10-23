from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ratings', on_delete=models.CASCADE)
    user =  models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.recipe.title} - {self.score} by {self.user.username}'

