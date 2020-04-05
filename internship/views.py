import json 
import pyperclip 
from django.contrib import messages
from django.shortcuts import render
from .career_utils import return_scraped_data, link_returner


def home(request):
    return render(request, 'internship/home.html', {'accessor': 'welcome homie'})

def list_internships(request):
    #context = {'accessor': return_scraped_data(25, 180, "Software")}
    context = {'accessor': {1: ['Tools Software Engineer intern', 'Intel', 'Hillsboro, OR', 'a month ago'], 2: ['Software Intern Developers, Applications', 'ALTEK', 'Ashburn, VA', '3 days ago'], 3: ['Hardware RF Software Dev. Intern', 'NOKIA', 'Dallas, TX', '16 days ago'], 4: ['Paid Internship - PHP/MySQL Full-Stack Software Developer', 'Dominion Enterprises', 'Beverly, MA', '14 days ago'], 5: ['Intern - Tools Software Engineer', 'Palo Alto Networks Inc.', 'Santa Clara, CA', '5 days ago'], 6: ['Software engineering intern (Biosensors) to help develop…', 'NeuroLeap Corp', 'San Jose, CA', '4 months ago'], 7: ['Intern, Development Tools Engineering', 'Roku', 'San Jose, CA', 'a month ago'], 8: ['Software Engineer - Intern', 'L3Harris Technologies', 'Tulsa, OK', '23 days ago'], 9: ['Software Engineer - Intern', 'L3Harris Technologies', 'Northampton, MA', '22 days ago'], 10: ['Software Engineer Intern', 'Viasat', 'Marlborough, MA', '15 days ago'], 11: ['Software Engineer - Intern', 'L3Harris Technologies', 'Camden, NJ', '24 days ago'], 12: ['High School Software Developer Intern', 'Geminid Systems', 'Milwaukee, WI', '2 months ago'], 13: ['Applications Development Intern', 'Banner Engineering', 'Minneapolis, MN', '25 days ago'], 14: ['Software Engineer Intern', 'Abaco Systems', 'Austin, TX', 'a month ago'], 15: ['Software Engineer Intern - Research Tools', '23Andme, Inc', 'Sunnyvale, CA', '21 days ago'], 16: ['Software Dev Cloud intern', 'NOKIA', 'Naperville, IL', '16 days ago'], 17: ['Intern, Database Systems Analyst Summer | Government', 'Trinet', 'Austin, TX', '13 days ago'], 18: ['Software Engineering Intern - AI/ML Applications', 'Adobe', 'San Jose, CA', 'a month ago'], 19: ['Software Developer Intern, Teams Tools And Services', 'Unity', 'Bellevue, WA', '11 days ago'], 20: ['Embedded Software Engineer Intern', 'Thales USA, Inc. (ATM)', 'Shawnee, KS', 'a month ago'], 21: ['Software Intern Advanced Applications', 'Intel', 'Santa Clara, CA', '6 days ago'], 22: ['Software Development Engineer Internship', 'Intel Corp.', 'Santa Clara, CA', '7 days ago'], 23: ['Intern, QA Software Engineer', 'Gigya', 'Palo Alto, CA', '15 days ago'], 24: ['Software Engineering Internship - Java', 'Red Hat', 'Raleigh, NC', '24 days ago'], 25: ['Software Engineering Intern', 'Open Learning Exchange', '', '3 days ago'], 26: ['Front End Software Engineer Intern', 'Chegg', 'San Francisco, CA', '12 days ago'], 27: ['Back End Software Engineer Intern', 'Chegg', 'Santa Clara, CA', '12 days ago'], 28: ['Back End Software Engineer Intern', 'Chegg', 'San Francisco, CA', '12 days ago'], 29: ['Sign-On Apprentice Software Architect/Software En', 'Raytheon', 'Aurora, CO', '18 days ago'], 30: ['Internships - Software Designer And Software Engin', 'TSYS', 'Columbus, GA', '11 days ago'], 31: ['Intern for - .Net - software development training and pr…', 'MNK Infotech', 'Irving, TX', 'a month ago'], 32: ['Software Engineering Intern', 'Tech Soft 3D', 'Berkeley, CA', 'a month ago'], 33: ['Intern, Software Engineer', 'Warner Bros. Entertainment Group', 'Burbank, CA', 'a month ago'], 34: ['Software Engineer - Intern', 'Think Surgical', 'Fremont, CA', 'a month ago'], 35: ['Software Developer Internship', 'Wycliffe Associates', 'Gainesville, FL', 'a month ago'], 36: ['SOFTWARE ENGINEER INTERN', 'StateServ', 'Birmingham, AL', 'a month ago'], 37: ['Software Developer Internship', 'Wycliffe Associates', 'Atlanta, GA', 'a month ago'], 38: ['Software Developer Internship', 'Wycliffe Associates', 'Tampa, FL', 'a month ago'], 39: ['Software Engineer Intern', 'Gartner, Inc.', 'Stamford, CT', 'a month ago'], 40: ['Intern-Software Engineer', 'Wyndham Destinations', 'Orlando, FL', 'a month ago'], 41: ['Software Developer Internship', 'Wycliffe Associates', 'Tallahassee, FL', 'a month ago'], 42: ['Software Engineer Intern', 'Experian', 'Allen, TX', 'a month ago'], 43: ['Software Developer Intern', 'Campus Risk Solutions', 'Hillsborough, CA', 'a month ago'], 44: ['Software Engineer Intern', 'Impinj', 'Seattle, WA', 'a month ago'], 45: ['Intern, Software Engineer', 'WarnerMedia', 'California, MD', 'a month ago'], 46: ['Software Developer Intern', 'Polyapp LLC', 'Minneapolis, MN', 'a month ago'], 47: ['Software Engineer Intern', 'Barco', 'Folsom, CA', 'a month ago'], 48: ['Software Engineer Intern', 'Vacasa', 'Boise, ID', 'a month ago'], 49: ['Software Intern', 'Waters Corporation', 'New Castle, DE', '25 days ago'], 50: ['Software Engineering Intern', 'Speedway Motorsports, Inc.', 'Lincoln, NE', 'a month ago']}}
    
    if request.method == 'POST':
        position_name = request.POST.get('position_name')
        company_name = request.POST.get('company_name')
        link = link_returner(position_name, company_name)
        pyperclip.copy(link)
        messages.success(request, 'The link to the company\'s career page has been copied to your clipboard.')
        
    return render(request, 'internship/internship_list.html', context)




