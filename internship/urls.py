from django.urls import path
from .views import (
    home,
    ListInternship,
    scrape_new_internships 
)

urlpatterns = [
    path('', home, name='internship_home'),
    path('internship/', ListInternship.as_view(), name='internship_list'),
    path('addInternships/', scrape_new_internships, name='internship_add'), 
   
]
