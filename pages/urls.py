from django.urls import path
from .views import about, index, page1

urlpatterns = [
    path('', index, name='ahmed'),
    path('about/', about, name='about'),
    path('page1/', page1, name='page1'),
]