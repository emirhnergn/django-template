from django.urls import path
from account.views import *

urlpatterns = [
    path('profile/<str:username>', ProfileDetailView.as_view(), name='profile'),
]