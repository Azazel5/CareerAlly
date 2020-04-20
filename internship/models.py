from django.db import models
from django.utils import timezone

class CompanyModel(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class InternshipModel(models.Model):
    position_name = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    days_ago_posted = models.CharField(max_length=100)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.company.id) + " | " + self.position_name + " | posID: " + str(self.id)
