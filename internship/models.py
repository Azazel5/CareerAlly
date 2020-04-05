from django.db import models
from django.utils import timezone


class InternshipModel(models.Model):
    position_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    days_ago_posted = models.CharField(max_length=100)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.company_name + " | " + self.position_name
