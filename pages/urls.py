from django.urls import path
from .views import about_view, change_view, search_view, explore_view


urlpatterns = [
    path('', about_view, name='about'),
    path('change/', change_view, name='change'),
    path('search/', search_view, name='search'),
    path('explore/', explore_view, name='explore')
]
