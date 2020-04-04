import json 
from django.shortcuts import render
from .career_utils import return_scraped_data


def list_internships(request):
    context = {'accessor': return_scraped_data(150, 180, "Software")}
    print(len(context))
    return render(request, 'internship/home.html', context)

