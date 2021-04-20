from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken import views
from .router import router



urlpatterns = [   
    path('auth/', views.obtain_auth_token, name='api-token-auth'),
    path('', include(router.urls))
]