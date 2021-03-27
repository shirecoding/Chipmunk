from api.models import (
    Account,
    Asset,
    CashAsset,
    ModelSerializerFactory,
    ModelViewSetFactory,
    Position,
    Share,
    StockAsset,
)
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", ModelViewSetFactory(User, ModelSerializerFactory(User)))
router.register(
    r"accounts", ModelViewSetFactory(Account, ModelSerializerFactory(Account))
)
router.register(
    r"positions", ModelViewSetFactory(Position, ModelSerializerFactory(Position))
)
router.register(r"assets", ModelViewSetFactory(Asset, ModelSerializerFactory(Asset)))
router.register(
    r"stock_assets", ModelViewSetFactory(StockAsset, ModelSerializerFactory(StockAsset))
)
router.register(
    r"cash_assets", ModelViewSetFactory(CashAsset, ModelSerializerFactory(CashAsset))
)
router.register(r"shares", ModelViewSetFactory(Share, ModelSerializerFactory(Share)))

urlpatterns = [
    path("", include(router.urls)),
]
