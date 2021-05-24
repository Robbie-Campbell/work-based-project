from django.shortcuts import render
from ..forms import D2AForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from OPAL.models import Patient
from ..models import D2A

@staff_member_required(login_url="/login/")
def D2A_create(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = D2AForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.patient = patient
            task = form.save()
            return redirect("services:D2A_list", patient.id)
    else:
        form = D2AForm()
    return render(request, "services/D2A/create.html", {"form":form, "patient": patient})


@staff_member_required(login_url="/login/")
def D2A_list(request, id):
    patient = Patient.objects.get(id=id)
    D2As = D2A.objects.filter(patient=patient).order_by("created_at")
    return render(request, "services/D2A/single.html", {"D2As":D2As})
