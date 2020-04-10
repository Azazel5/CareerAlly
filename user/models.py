from django.db import models
from django.contrib.auth.models import User 
from internship.models import InternshipModel 

class UserInternshipProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    internships_applied = models.ForeignKey(InternshipModel, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username + ' - ' + f'({self.internships_applied.pk}) ' + self.internships_applied.position_name
