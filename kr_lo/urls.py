from django.urls import path
from .views import index,krill,lotin
urlpatterns=[
    path('kiril-lotin/',krill, name='krill'),
    path('lotin-kiril/',lotin, name='lotin'),
    path('',index, name='index')
]