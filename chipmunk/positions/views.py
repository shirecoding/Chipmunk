from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import redirect, render
from django_pandas.io import read_frame

from .models import Account, Position


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ["name", "symbol", "account", "shares", "cost_basis"]


@login_required(login_url="login")
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


@login_required(login_url="login")
def position(request):
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Position.objects.create(**data).save()

            return redirect("/positions")
    else:
        form = PositionForm()
        return render(request, "positions/position.html", {"form": form})
