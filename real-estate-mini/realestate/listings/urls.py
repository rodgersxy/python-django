# listings/urls.py

from django.urls import path
from .views import listing_list

urlpatterns = [
    path('listings/', listing_list, name='listing_list'),
]
