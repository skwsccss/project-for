from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
