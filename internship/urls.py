from django.urls import path
from .views import (
    ListInternship,
    scrape_new_internships, 
)

urlpatterns = [
    path('', ListInternship.as_view(), name='internship_list'),
    path('addInternships/', scrape_new_internships, name='internship_add'), 
]
