from django.urls import path
from . import views

app_name="OPAL"

urlpatterns = [

    # Patient URLS
    path("patient/<int:id>/", views.patient_single, name="patient_single"),
    path("patient/", views.patient_list, name="patient_list"),
    path("patient/search/", views.patient_search, name="patient_search"),
    path("patient/create/", views.patient_create, name="patient_create"),
    path("patient/edit/<int:id>/", views.patient_edit, name="patient_edit"),
    path("patient/delete/<int:id>/", views.patient_delete, name="patient_delete"),
    
    # Therapist URLS
    path("therapist/<int:id>/", views.therapist_single, name="therapist_single"),
    path("therapist/", views.therapist_list, name="therapist_list"),
    path("therapist/search/", views.therapist_search, name="therapist_search"),
    path("therapist/create/", views.therapist_create, name="therapist_create"),
    path("therapist/edit/<int:id>/", views.therapist_edit, name="therapist_edit"),
    path("therapist/delete/<int:id>/", views.therapist_delete, name="therapist_delete"),
    
    # Therapy URLS
    path("therapy/<int:id>/", views.therapy_single, name="therapy_single"),
    path("therapy/", views.therapy_list, name="therapy_list"),
    path("therapy/search/", views.therapy_search, name="therapy_search"),
    path("therapy/create/<int:id>/", views.therapy_create, name="therapy_create"),
    path("therapy/edit/<int:id>/", views.therapy_edit, name="therapy_edit"),
    path("therapy/delete/<int:id>/", views.therapy_delete, name="therapy_delete"),
]