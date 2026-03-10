# gstaf/models.py
from django.db import models

class Poste(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    departement = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE)  # 🔹 relation avec Poste
    email = models.EmailField()
    date_embauche = models.DateField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"
class TacheCarriere(models.Model):
    PLANIFICATION = 'planification'
    FORMATION = 'formation'
    PROMOTION = 'promotion'

    TYPES_TACHE = [
        (PLANIFICATION, 'Planification'),
        (FORMATION, 'Formation'),
        (PROMOTION, 'Promotion'),
    ]

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name="taches_carriere")
    type_tache = models.CharField(max_length=20, choices=TYPES_TACHE)
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.get_type_tache_display()} - {self.titre} ({self.employe.nom})"