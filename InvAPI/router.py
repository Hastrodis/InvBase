from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('tech', views.TechViewSet)
router.register('hist', views.HistViewSet)
router.register('type', views.TypeViewSet)
router.register(
    prefix = 'search',
    basename='search',
    viewset=views.SearchViewSet
)