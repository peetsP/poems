"""
This script is used to create models for this app
Author: Peter Murimi
Date: 4/23/2020
"""
from django.shortcuts import render


def index(request):
    """
    Index Module
    """

    return render(request, 'index.html')
