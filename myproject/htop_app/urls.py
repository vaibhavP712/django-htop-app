from django.urls import path
from .views import htop_view

urlpatterns = [
    path('htop/', htop_view, name='htop_view'),
]
