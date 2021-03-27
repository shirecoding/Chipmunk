from django.contrib.auth.models import User
from django.db import models
from rest_framework import routers, serializers, viewsets

################################################################################################
## User
################################################################################################


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
