from . import views
from django.urls import path

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    # path('projects/', views.projects, name='projects'),
]
