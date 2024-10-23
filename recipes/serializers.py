from rest_framework import serializers
from .models import Recipe, Category, Rating


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'category', 'author', 'created_at',
                  'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'user', 'score']
