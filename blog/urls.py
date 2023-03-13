from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blogs, name="all_blogs"),
    path('<int:blog_id>/', views.detail, name="blog_detail")
]

