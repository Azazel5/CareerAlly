from django.shortcuts import render
from .internship import return_scraped_data


def list_internships(request):
    context = return_scraped_data(150, 180, "Software")

