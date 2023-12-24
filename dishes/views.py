from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import SVGFile, Category, Dish
from .serializers import SVGSerializer, CategorySerializer, DishSerializer

class SVGFileView(ListCreateAPIView):
    queryset = SVGFile.objects.all()
    serializer_class = SVGSerializer

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer