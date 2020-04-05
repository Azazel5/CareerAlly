import json 
import pyperclip 

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView 
from django.shortcuts import redirect
from datetime import datetime

from .models import InternshipModel 
from .career_utils import return_scraped_data, link_returner


def home(request):
    return render(request, 'internship/home.html', {'accessor': 'welcome homie'})

class ListInternship(ListView):
    model = InternshipModel
    template_name = 'internship/internship_list.html'
    context_object_name = 'internship_list'

    def post(self, request, *args, **kwargs):
        position_name = request.POST.get('position_name')
        company_name = request.POST.get('company_name')
        link = link_returner(position_name, company_name)
        pyperclip.copy(link)
        messages.success(request, 'The link to the company\'s career page has been copied to your clipboard.')
        return redirect('internship_list')


def scrape_new_internships(request):
    context = {'accessor': return_scraped_data(25, 180, "Software")}
    inner_dict = list(context.values())[0]
    for key in inner_dict:
        obj = InternshipModel.objects.get_or_create(
            position_name=inner_dict[key][0],
            company_name=inner_dict[key][1],
            location=inner_dict[key][2],
            days_ago_posted= inner_dict[key][3]
        )

    return render(request, 'internship/add_to_database.html', {'accessor': 'Added to database'})

# Have to validate my results properly before adding it to the database 
# Check if the response you get from the function is proper before seding it into the table 
# To kill port -> sudo lsof -i tcp:8000