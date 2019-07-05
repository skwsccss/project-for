from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Movie, Users


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'year')


class UsersS(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'email')
