from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """The home page for Blog"""
    return render(request, 'blogs/index.html')


@login_required
def blogs(request):
    """Show all blogs."""
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


@login_required
def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:blogs'))

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    """Edit an existing blog."""
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(request, blog)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current blog.
        form = BlogPostForm(instance=blog)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogs'))

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)


def check_blog_owner(request, blog):
    """Check currently logged-in user"""
    if blog.owner != request.user:
        raise Http404
