from django.forms import ModelForm
from django import forms
from . models import Patient, Therapy, Therapist

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class TherapyForm(ModelForm):
    class Meta:
        model = Therapy
        fields = "__all__"
        exclude = ["patient"]

class TherapistForm(ModelForm):
    class Meta:
        model = Therapist
        fields = "__all__"