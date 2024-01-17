from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import *


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'fam', 'name', 'otc', 'phone')
        verbose_name = 'Турист'


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude', 'height')
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')
        verbose_name = 'Уровень сложности'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('data', 'title')
        verbose_name = 'Фото'


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coordinates = CoordinatesSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coordinates', 'level',
            'images', 'status')
        read_only_fields = ['status']


