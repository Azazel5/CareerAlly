from django.urls import path
from .views import list_internships 

urlpatterns = [
    path('', list_internships, name='internship-list'),
]
