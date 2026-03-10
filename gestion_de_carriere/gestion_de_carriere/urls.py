# gestion_de_carriere/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # interface d'administration
    path('', include('gstaf.urls')),         # redirige vers les URLs de ton app gstaf
]