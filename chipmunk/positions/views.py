from django.shortcuts import render
from .models import Account, Position
from django_pandas.io import read_frame


def home(request):

    positions = Position.objects.all()

    df = read_frame(positions)
    
    return render(request, 'positions/home.html', {'pandas_html': df.to_html()})