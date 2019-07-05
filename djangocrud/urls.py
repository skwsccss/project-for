
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from djangocrud.api import views
from .api.controllers import main
from .api.views import *

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'users', views.UserView)


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('contracts', ContractsView.as_view(), name='contracts'),
    path('admin', admin.site.urls),
    # path('movies', main.index),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]