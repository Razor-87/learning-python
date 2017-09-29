"""Defines URL patterns for pizzas."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all pizzas.
    url(r'^pizzas/$', views.pizzas, name='pizzas'),

    # Detail page for a single pizza.
    url(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
]
