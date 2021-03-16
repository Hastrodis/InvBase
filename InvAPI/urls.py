from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ausers', views.UserViewSet)
router.register(r'atech', views.TechViewSet)
router.register(r'ahist', views.HistViewSet)
router.register(r'atype', views.TypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]