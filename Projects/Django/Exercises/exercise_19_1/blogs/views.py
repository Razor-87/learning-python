from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """The home page for Blog"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def edit_blog(request, blog_id):
    """Edit an existing blog."""
    blog = BlogPost.objects.get(id=blog_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current blog.
        form = BlogPostForm(instance=blog)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:edit_blog',
                                        args=[blog.id]))

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
