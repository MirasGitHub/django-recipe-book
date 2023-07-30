import json

from recipe.models import Recipe

# python3 manage.py runscript populate_database


def run():

    file = "/home/miranda/Desktop/SkillWill homeworks/recipe_book/scripts/mock_data.json"
    mock_data = open(file)
    data = json.load(mock_data)['data']
    for recipe in data:
        Recipe.objects.create(**recipe)
