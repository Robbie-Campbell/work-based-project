from django.forms import ModelForm
from django import forms
from . models import Pathway, ReferralSource, D2A

class PathwayForm(ModelForm):
    admission_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    class Meta:
        model = Pathway
        fields = "__all__"
        exclude = ["patient"]

class ReferralForm(ModelForm):
    class Meta:
        model = ReferralSource
        fields = "__all__"

class D2AForm(ModelForm):
    D2A_completion_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                          input_formats=('%d/%m/%Y',))
    class Meta:
        model = D2A
        fields = "__all__"
        exclude = ["patient"]