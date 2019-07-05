from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import MovieSerializer, UsersS
from .models import Movie
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
import jwt
from ..settings import SECRET_KEY
from rest_framework_jwt.settings import api_settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersS

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        #check user in db
        user_obj = User.objects.filter(username__exact=username).first()
        if user_obj:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(username=username, password=password)
                if user:
                    # return JWT token
                    payload = jwt_payload_handler(user)
                    msg = {
                        'token': jwt.encode(payload, SECRET_KEY),
                        'status': 'success',
                        'user': {
                            "username": user_obj.username,
                            "firstname": user_obj.first_name,
                            "lastname": user_obj.last_name,
                            "email": user_obj.email

                        }
                    }
                    return Response(msg, status=status.HTTP_200_OK)
                else:
                    return Response(
                        {
                            'error': 'invalid Credential',
                            'status': 'failed'
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                msg = {
                    'message': 'Must include username and "password".',
                    'status': 'failed',
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            msg = {
                'message': 'Account with this username does not exists',
                'status': 'failed'
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)


class ContractsView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)