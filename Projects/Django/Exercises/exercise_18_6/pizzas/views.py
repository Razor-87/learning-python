from django.shortcuts import render


def index(request):
    """The home page for Learning Log"""
    return render(request, 'pizzas/index.html')
