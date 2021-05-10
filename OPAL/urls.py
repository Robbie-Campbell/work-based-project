from django.urls import path, include
from . import views


urlpatterns = [
    path("patient/<int:id>/", views.patient_single, name="patient_single"),
    path("patient/", views.patient_list, name="patient_list"),
    path("patient/create/", views.patient_create, name="patient_create"),
    path("patient/delete/<int:id>/", views.patient_delete, name="patient_delete"),
    path("therapist/<int:id>/", views.therapist_single, name="therapist_single"),
    path("therapist/", views.therapist_list, name="therapist_list"),
    path("therapist/create/", views.therapist_create, name="therapist_create"),
    path("therapist/delete/<int:id>/", views.therapy_delete, name="therapist_delete"),
    path("therapy/<int:id>/", views.therapy_single, name="therapy_single"),
    path("therapy/", views.therapy_list, name="therapy_list"),
    path("therapy/create/", views.therapy_create, name="therapy_create"),
    path("therapy/delete/<int:id>/", views.therapy_delete, name="therapy_delete"),
]