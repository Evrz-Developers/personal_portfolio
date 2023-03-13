from django.shortcuts import render
from .models import Project, Skill
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from custom_users.models import CustomUser


def home(request):
    user_obj = CustomUser.objects.all()
    project_obj = Project.objects.all()
    skill_obj = Skill.objects.all()
    return render(request, 'index.html',
                  {'projects': project_obj, 'users': user_obj,
                   'skills': skill_obj})


# def projects(request):
#     user_obj = CustomUser.objects.all()
#     project_obj = Project.objects.all()
#     return render(request, 'index.html',
#                   {'projects': project_obj, 'users': user_obj})
