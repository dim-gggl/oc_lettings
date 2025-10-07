"""
Views for the lettings application.

Functions:
    lettings_index: View to display the list of lettings.
    letting: View to display a letting's details.
"""

from django.shortcuts import render
from .models import Letting


# Create your views here.
def lettings_index(request):
    """
    View to display the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/lettings_index.html', context)


def letting(request, letting_id):
    """
    View to display a letting's details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
