from django.urls import path
from .views import list_internships, home

urlpatterns = [
    path('', home, name='internship_home'),
    path('internship/', list_internships, name='internship_list'),
]
