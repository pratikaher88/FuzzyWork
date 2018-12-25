from django.urls import path
from .views import  new_entry, display_output, list_entries


urlpatterns=[

path('',new_entry, name='new-entry'),
path('output', display_output, name='output'),
path('listentries', list_entries, name='list-entries')

]