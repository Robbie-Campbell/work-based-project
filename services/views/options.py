from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from OPAL.models import Patient

@staff_member_required(login_url="/login/")
def add_service(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, "services/add_service.html", {"patient": patient})

@login_required
def view_services(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, "services/view_services.html", {"patient": patient})
