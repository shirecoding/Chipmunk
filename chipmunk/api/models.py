from django.db import models
from rest_framework import routers, serializers, viewsets


def ModelSerializerFactory(model):

    return type(
        f"{model.__name__}Serializer",
        (serializers.ModelSerializer,),
        {"Meta": type("Meta", (object,), {"model": model, "fields": "__all__"})},
    )


def ModelViewSetFactory(model, serializer):

    return type(
        f"{model.__name__}ViewSet",
        (viewsets.ModelViewSet,),
        {"queryset": model.objects.all(), "serializer_class": serializer},
    )


################################################################################################
## Share
################################################################################################

UNITS = [
    ("SGD", "Singapore Dollar"),
    ("USD", "US Dollar"),
    ("BTC", "Bitcoin"),
    ("ETH", "Ethereum"),
]


class Share(models.Model):
    """Share"""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    unit = models.ForeignKey("Share", on_delete=models.CASCADE)


################################################################################################
## Asset
################################################################################################


class Asset(models.Model):
    """Assest"""

    name = models.CharField(max_length=100)
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    num_shares = models.FloatField(default=0.0)
    notes = models.TextField()

    def __str__(self):
        return self.name


class StockAsset(Asset):
    """Stock Asset"""

    brokerage = models.CharField(max_length=100)


class CashAsset(Asset):
    """Cash Asset"""

    bank = models.CharField(max_length=100)


################################################################################################
## Account
################################################################################################


class Account(models.Model):
    """Brokerage account"""

    ACCOUNT_TYPES = (
        ("TRADITIONAL", "Traditional IRA or 401(k)"),
        ("ROTH", "Roth IRA or 401(k)"),
        ("STANDARD", "Standard Brokerage"),
    )

    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100, choices=ACCOUNT_TYPES)
    cash_balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


################################################################################################
## Position
################################################################################################


class Position(models.Model):
    """Position eg. equity holding"""

    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    shares = models.FloatField()
    cost_basis = models.FloatField(default=0.0)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    def __str__(self):
        return self.symbol
