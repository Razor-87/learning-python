from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Page for adding a new blog.
    url(r'^new_blog/$', views.new_blog, name='new_blog'),

    # Page for editing an blog.
    url(r'^edit_blog/(?P<blog_id>\d+)/$', views.edit_blog,
        name='edit_blog'),
]
