from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_employes, name='home'),  # ← nouvelle route pour /
    path('employes/', views.liste_employes, name='liste_employes'),
    path('employes/ajouter/', views.ajouter_employe, name='ajouter_employe'),
    path('employes/<int:pk>/modifier/', views.modifier_employe, name='modifier_employe'),
    path('employes/<int:pk>/supprimer/', views.supprimer_employe, name='supprimer_employe'),
    path('postes/', views.liste_postes, name='liste_postes'),
    path('postes/ajouter/', views.ajouter_poste, name='ajouter_poste'),
    path('postes/<int:pk>/modifier/', views.modifier_poste, name='modifier_poste'),
    path('postes/<int:pk>/supprimer/', views.supprimer_poste, name='supprimer_poste'),
    path('', views.home, name='home'),
    path('taches-carriere/', views.liste_taches_carriere, name='liste_taches_carriere'),
    path('taches-carriere/ajouter/', views.ajouter_tache_carriere, name='ajouter_tache_carriere'),
]
