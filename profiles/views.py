"""
Views for the profiles application.

Functions:
    profiles_index: View to display the list of profiles.
    profile: View to display a profile's details.
"""

from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    View to display the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/profiles_index.html', context)


def profile(request, username):
    """
    View to display a profile's details.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
