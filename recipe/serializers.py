from django.contrib.auth.models import User
from rest_framework import serializers

from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'ingredient',
            'time',
            'process',
            'user'
        )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

        read_only_fields = ['token']
