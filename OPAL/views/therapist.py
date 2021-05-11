from django.shortcuts import render
from ..models import Therapy, Therapist
from ..forms import TherapistForm
from django.db.models import Avg, Q
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def therapist_list(request):
    therapists = Therapist.objects.all()
    return render(request, "OPAL/therapist/list.html", {"therapists": therapists})
    
@login_required
def therapist_single(request, id):
    therapist = Therapist.objects.get(id=id)
    therapies = Therapy.objects.filter(therapist=id)
    indirect_average = therapies.aggregate(Avg('indirect_time'))
    direct_average = therapies.aggregate(Avg('direct_time'))
    return render(request, "OPAL/therapist/single.html", {"therapist": therapist, "therapies": therapies, "direct_average": direct_average["direct_time__avg"], "indirect_average": indirect_average["indirect_time__avg"]})

@staff_member_required(login_url="/login/")
def therapist_create(request):
    if request.method == "POST":
        form = TherapistForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("therapist_single", id=task.id)
    else:
        form = TherapistForm()
    return render(request, "OPAL/therapist/create.html", {"form":form})

@staff_member_required(login_url="/login/")
def therapist_edit(request, id):
    therapist = Therapist.objects.get(id=id)

    if request.method == "POST":
        form = TherapistForm(request.POST, instance=therapist)
        if form.is_valid():
            form.save()
            return redirect("therapist_single", id=id)
    else:
        data = {"first_name": therapist.first_name, "surname": therapist.surname, 
                "Therapist_role": therapist.therapist_role, "band": therapist.band, 
                "assigned_team": therapist.assigned_team}
        form = TherapistForm(initial=data)
    return render(request, "OPAL/therapist/edit.html", {"form":form, "therapist": therapist})

@staff_member_required(login_url="/login/")
def therapist_delete(request, id):
    therapist = Therapist.objects.get(id=id)
    therapist.delete()
    return redirect('therapist_list')

@login_required
def therapist_search(request):
    q = request.GET.get('q')
    object_list = Therapist.objects.filter(
        Q(first_name__icontains=q) | Q(surname__icontains=q) | Q(id__icontains=q)
    )
    return render(request, 'OPAL/therapist/list.html', {"therapists": object_list})
