from django.forms import ModelForm
from django import forms
from . models import Pathway, ReferralSource, D2A, Referral, Discharge, DischargeService

'''
    Form to input a pathway
'''
class PathwayForm(ModelForm):
    admission_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    class Meta:
        model = Pathway
        fields = "__all__"
        exclude = ["patient"]

'''
    Form to input a Referral Source
'''
class ReferralSourceForm(ModelForm):
    class Meta:
        model = ReferralSource
        fields = "__all__"

'''
    Form to input a Discharge
'''
class DischargeForm(ModelForm):
    date_no_reside = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
                                 
    discharge_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    class Meta:
        model = Discharge
        fields = "__all__"
        exclude = ["patient"]

'''
    Form to input a Discharge Service
'''
class DischargeServiceForm(ModelForm):
    class Meta:
        model = DischargeService
        fields = "__all__"

'''
    Form to input a Referral
'''
class ReferralForm(ModelForm):
    referral_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                     input_formats=('%d/%m/%Y',))
    initial_contact_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                     input_formats=('%d/%m/%Y',))
    class Meta:
        model = Referral
        fields = "__all__"
        exclude = ["patient"]

'''
    Form to input a D2A
'''
class D2AForm(ModelForm):
    D2A_completion_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                          input_formats=('%d/%m/%Y',))
    class Meta:
        model = D2A
        fields = "__all__"
        exclude = ["patient"]