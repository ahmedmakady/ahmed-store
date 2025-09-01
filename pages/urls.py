from django.urls import path
from .views import about, index

urlpatterns = [
    path('', index, name='ahmed'),
    path('about/', about, name='about'),
]