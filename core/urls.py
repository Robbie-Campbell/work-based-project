from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html")),
    path('about/', TemplateView.as_view(template_name="about.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT);