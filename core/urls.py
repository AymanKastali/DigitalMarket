from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('browse/', browse, name='browse'),
    path('favorites/', favorites, name='favorites'),
    path('bookmarks/', bookmarks, name='bookmarks'),
    path('ads/', ads, name='ads'),
]