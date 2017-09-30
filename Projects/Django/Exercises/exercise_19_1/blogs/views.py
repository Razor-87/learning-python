from django.shortcuts import render

from .models import BlogPost


def index(request):
    """The home page for Blog"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)
