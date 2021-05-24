from django.shortcuts import render
from ..forms import PathwayForm, ReferralForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from OPAL.models import Patient
from ..models import Pathway

@staff_member_required(login_url="/login/")
def pathway_create(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = PathwayForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.patient = patient
            task = form.save()
            return redirect("services:pathway_list", patient.id)
    else:
        form = PathwayForm()
    return render(request, "services/pathways/create.html", {"form":form, "patient": patient})

@staff_member_required(login_url="/login/")
def referral_create(request, id):
    if request.method == "POST":
        form = ReferralForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("services:pathway_create", id=id)
    else:
        form = ReferralForm()
    return render(request, "services/pathways/referral_source/create.html", {"form":form})

@staff_member_required(login_url="/login/")
def pathway_list(request, id):
    patient = Patient.objects.get(id=id)
    pathways = Pathway.objects.filter(patient=patient).order_by('-created_at')
    return render(request, "services/pathways/list.html", {"pathways":pathways, "patient": patient})

