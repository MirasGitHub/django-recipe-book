from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer, RegisterSerializer, UserSerializer


# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data)

        return Response({'error': "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request):
        recipes = request.user.recipe.all()
        serializer = self.serializer_class(instance=recipes, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeSingletonView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializer

    def get(self, request, pk):
        post = get_object_or_404(Recipe, pk=pk)
        serializer = self.serializer_class(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        post = get_object_or_404(Recipe, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=post, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
