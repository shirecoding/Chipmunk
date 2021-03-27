from api.models import AccountViewSet, PositionViewSet, UserViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"positions", PositionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
