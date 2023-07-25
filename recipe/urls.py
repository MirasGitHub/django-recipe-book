from django.urls import path, include
from rest_framework import routers

from recipe import views

router = routers.DefaultRouter()
router.register('recipe', views.RecipeView)
urlpatterns = [
    path('', include(router.urls))
]
