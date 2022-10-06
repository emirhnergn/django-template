from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),
    path('category/<slug:categorySlug>', CategoryListView.as_view(), name='category'),
]