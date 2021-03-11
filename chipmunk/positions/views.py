from django.shortcuts import render
from django_pandas.io import read_frame

from .models import Account, Position


def home(request):

    positions = Position.objects.all()
    accounts = Account.objects.all()

    positions_df = read_frame(positions)[
        ["name", "symbol", "account", "shares", "cost_basis"]
    ]
    accounts_df = read_frame(accounts)[["name", "account_type", "cash_balance"]]

    return render(
        request,
        "positions/home.html",
        {
            "positions_df": positions_df.to_html(index=False),
            "accounts_df": accounts_df.to_html(index=False),
        },
    )
