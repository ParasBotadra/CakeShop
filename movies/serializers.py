from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        ingridients = representation['ingridients']
        list_ing = []
        for ing in ingridients:
            list_ing.append(ing.name)
        representation['ingridients'] = list_ing
        return representation
