from django.shortcuts import render, get_object_or_404
from .models import Blog
from custom_users.models import CustomUser


# Create your views here.
def blogs(request):
    blog_obj = Blog.objects.order_by('-created_at')
    user_obj = CustomUser.objects.all()
    # blog_obj = Blog.objects.order_by('-date')[:5]
    return render(request, 'blogs.html', {'blogs': blog_obj, 'users': user_obj})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})
