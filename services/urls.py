from django.urls import path
from . import views

app_name="services"

urlpatterns = [
    # Options URL
    path("<int:id>/", views.service_options, name="service_options"),
    
    # Pathway URLS
    path("pathways/create/<int:id>/", views.pathway_create, name="pathway_create"),
    path("pathways/list/<int:id>/", views.pathway_list, name="pathway_list"),
    path("referral/create/<int:id>/", views.referral_create, name="referral_create"),

    # D2A URLS
    path("D2A/create/<int:id>/", views.D2A_create, name="D2A_create"),
    path("D2A/list/<int:id>/", views.D2A_list, name="D2A_list"),
]