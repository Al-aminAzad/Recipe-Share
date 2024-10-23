from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, RecipeListCreateView, RecipeDetailView, RatingListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
]
