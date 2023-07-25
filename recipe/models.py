from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=400)
    ingredient = models.CharField(max_length=1000)
    time = models.FloatField()
    process = models.TextField()

    def __str__(self):
        return self.name
