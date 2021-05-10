from django.shortcuts import render
from . models import Patient, Therapy, Therapist
from .forms import PatientForm, TherapyForm, TherapistForm
from django.db.models import Avg
from django.shortcuts import redirect

def patient_single(request, id):
    patient = Patient.objects.get(id=id)
    therapies = Therapy.objects.filter(patient=id)
    indirect_average = therapies.aggregate(Avg('indirect_time'))
    direct_average = therapies.aggregate(Avg('direct_time'))
    return render(request, "OPAL/patient/single.html", {"patient": patient, "therapies": therapies, "direct_average": direct_average["direct_time__avg"], "indirect_average": indirect_average["indirect_time__avg"]})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "OPAL/patient/list.html", {"patients": patients})

def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("patient_single", id=task.id)
    else:
        form = PatientForm()
    return render(request, "OPAL/patient/create.html", {"form":form})

def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')

def therapy_single(request, id):
    therapy = Therapy.objects.get(id=id)
    return render(request, "OPAL/therapy/single.html", {"therapy": therapy})

def therapy_list(request):
    therapies = Therapy.objects.all()
    return render(request, "OPAL/therapy/list.html", {"therapies": therapies})


def therapy_create(request):
    if request.method == "POST":
        form = TherapyForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("therapy_single", id=task.id)
    else:
        form = TherapyForm()
    return render(request, "OPAL/therapy/create.html", {"form":form})

def therapy_delete(request, id):
    therapy = Therapy.objects.get(id=id)
    therapy.delete()
    return redirect('therapy_list')

def therapist_list(request):
    therapist = Therapist.objects.all()
    return render(request, "OPAL/therapist/list.html", {"therapist": therapist})   

def therapist_single(request, id):
    therapist = Therapist.objects.get(id=id)
    therapies = Therapy.objects.filter(therapist=id)
    indirect_average = therapies.aggregate(Avg('indirect_time'))
    direct_average = therapies.aggregate(Avg('direct_time'))
    return render(request, "OPAL/therapist/single.html", {"therapist": therapist, "therapies": therapies, "direct_average": direct_average["direct_time__avg"], "indirect_average": indirect_average["indirect_time__avg"]})
 
 
def therapist_create(request):
    if request.method == "POST":
        form = TherapistForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("therapist_single", id=task.id)
    else:
        form = TherapistForm()
    return render(request, "OPAL/therapist/create.html", {"form":form})

def therapist_delete(request, id):
    therapist = Therapist.objects.get(id=id)
    therapist.delete()
    return redirect('therapist_list')