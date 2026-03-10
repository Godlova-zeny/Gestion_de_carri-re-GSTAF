from django.contrib import admin
from .models import Employe, Poste, TacheCarriere   # ← ajoute TacheCarriere ici

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste', 'date_embauche')
    search_fields = ('nom', 'poste__titre')
    list_filter = ('poste', 'date_embauche')

class PosteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'departement')
    search_fields = ('titre', 'departement')
    list_filter = ('departement',)

class TacheCarriereAdmin(admin.ModelAdmin):
    list_display = ('type_tache', 'titre', 'employe', 'date')
    search_fields = ('titre', 'employe__nom')
    list_filter = ('type_tache', 'date')

admin.site.register(Employe, EmployeAdmin)
admin.site.register(Poste, PosteAdmin)
admin.site.register(TacheCarriere, TacheCarriereAdmin)