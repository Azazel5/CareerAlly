import json 
import pyperclip 
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView 
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .models import InternshipModel, CompanyModel 
from .career_utils import return_scraped_data, link_returner


class ListInternship(LoginRequiredMixin, ListView):
    login_url = 'login'

    model = InternshipModel
    template_name = 'internship/internship_list.html'
    context_object_name = 'internship_list'
    paginate_by = 10
    ordering = ['-date_added']

    def post(self, request, *args, **kwargs):
        if 'link_button' in request.POST:
            position_name = request.POST.get('position_name')
            company_name = request.POST.get('company_name')
            link = link_returner(position_name, company_name)
            pyperclip.copy(link)
            messages.success(request, 'The link to the company\'s career page has been copied to your clipboard.')
            return redirect('internship_list')
        elif 'add_button' in request.POST:
            internship = request.POST.get('internship_pk')
            request.session['internship_pk'] = internship
            return redirect('user_info')

@login_required()
def scrape_new_internships(request):
    context = {'accessor': return_scraped_data(25, 180, "Software")}
    inner_dict = list(context.values())[0]
    for key in inner_dict:
        company, created_tuple = CompanyModel.objects.get_or_create(
            company_name=inner_dict[key][0]
        )
        position, created_tuple = InternshipModel.objects.get_or_create(
            position_name=key,
            company=company,
            location=inner_dict[key][1],
            days_ago_posted= inner_dict[key][2],
        )

    return render(request, 'internship/add_to_database.html', {'accessor': 'Added to database'})

# Have to validate my results properly before adding it to the database 
# Check if the response you get from the function is proper before seding it into the table 
# To kill port -> sudo lsof -i tcp:8000

