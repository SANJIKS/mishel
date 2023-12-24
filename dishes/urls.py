from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet, CategoryView, SVGFileView

router = DefaultRouter()
router.register('dishes', DishViewSet, basename='dish')
# router.register('categories', CategoryView, basename='category')
# router.register('svgs', SVGFileView, basename='svg-file')


urlpatterns =[
    path('',include(router.urls)),
    path('categories/', CategoryView.as_view()),
    path('svgs/',  SVGFileView.as_view())
]