from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UserInternshipProfile  
from internship.models import InternshipModel


@login_required()
def user_view(request):
# Gets the session object from the internship application view and adds it to the database
# Does the usual checks to make sure duplication isn't an issue. 
    req_object = request.session.get('internship_pk')
    notes_object = request.session.get('internship_notes')
    recent_user_application = None
    if req_object != None and notes_object == '':
        internship_pk = int(req_object)
        internship = InternshipModel.objects.get(pk=internship_pk)
        recent_user_application, created = UserInternshipProfile.objects.get_or_create(
            user=request.user, internships_applied=internship, notes=None)
   
    elif req_object != None and notes_object != '':
        internship_pk = int(req_object)
        internship = InternshipModel.objects.get(pk=internship_pk)
        recent_user_application, created = UserInternshipProfile.objects.get_or_create(
            user=request.user, internships_applied=internship, notes=notes_object)

    
    user = UserInternshipProfile.objects.filter(user=request.user)
    num_applications = user.count()

    return render(request, 'user/user.html', context={
        'user_obj': user,
        'num_applications': num_applications,
        'recent_application': recent_user_application
    })