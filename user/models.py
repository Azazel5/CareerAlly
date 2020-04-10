from django.db import models
from django.contrib.auth.models import User 
from internship.models import InternshipModel 

class UserInternshipProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    application_count = models.IntegerField(blank=True, null=True)
    internships_applied = models.ForeignKey(InternshipModel, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return user.username
