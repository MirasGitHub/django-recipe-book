from django.urls import path, include
from rest_framework import routers

from recipe import views
from recipe.views import RegisterView, LoginView, LogoutView, RecipeList, RecipeDetail

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('recipes/', RecipeList.as_view(), name='recipes'),
    path('recipes/<int:pk>', RecipeDetail.as_view(), name='recipe detail'),
]
