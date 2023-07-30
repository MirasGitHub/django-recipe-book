from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Recipe(models.Model):
    name = models.CharField(max_length=400)
    ingredient = models.CharField(max_length=1000)
    time = models.FloatField()
    process = models.TextField()
    slug = models.SlugField(null=False, unique=False, default='slug')
    user = models.ForeignKey(User, related_name='recipe', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ["-id"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


def create_user(self, username, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(username, email, password, **extra_fields)


@property
def token(self):
    token1 = jwt.encode(
        {'username': self.username, 'email': self.email,
         'exp': datetime.utcnow() + timedelta(hours=24)},
        settings.SECRET_KEY, algorithm='HS256')
    return token1
