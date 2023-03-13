from django.shortcuts import render
from .models import Project
from custom_users.models import CustomUser


# Create your views here.
def home(request):
    user_obj = CustomUser.objects.all()
    project_obj = Project.objects.all()
    return render(request, 'index.html',
                  {'projects': project_obj, 'users': user_obj})


def projects(request):
    user_obj = CustomUser.objects.all()
    project_obj = Project.objects.all()
    return render(request, 'index.html',
                  {'projects': project_obj, 'users': user_obj})
