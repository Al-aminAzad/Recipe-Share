from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Recipe, Category, Rating
from .permissions import IsAuthorOrReadOnly
from .serializers import RecipeSerializer, CategorySerializer, RatingSerializer


# Create your views here.

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@method_decorator(cache_page(60*5), name='dispatch')
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'description']


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthorOrReadOnly]


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
