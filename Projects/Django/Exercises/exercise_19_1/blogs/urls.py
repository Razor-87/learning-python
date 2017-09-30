from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # # Page for adding a new entry.
    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # # Page for editing an entry.
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    #     name='edit_entry'),
]
