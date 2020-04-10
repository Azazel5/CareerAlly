from django.urls import path
from .views import user_view

urlpatterns = [
    path('', user_view, name='user_info'),
]
