from django.db import models
from django.urls import reverse
from OPAL.models import Patient, Therapist

class ReferralSource(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pathway(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    meet_criteria_therapy = RAFT = models.BooleanField(default=False)
    referral_source = models.ForeignKey(ReferralSource, on_delete=models.CASCADE)
    front_door = models.BooleanField(default=False)
    RAFT = models.BooleanField(default=False)
    CCMT = models.BooleanField(default=False)
    CCMT_Date = models.DateField(blank=True, null=True)
    admission_barthel = models.IntegerField(blank=True, null=True)
    discharge_barthel = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.surname}: Pathway"

class D2A(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapist_completing_d2a = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    D2A_completion_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.surname}: D2A"