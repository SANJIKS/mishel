from rest_framework import serializers
from .models import SVGFile, Category, Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

class SVGSerializer(serializers.ModelSerializer):
    class Meta:
        model = SVGFile
        fields = ('svg_file',)