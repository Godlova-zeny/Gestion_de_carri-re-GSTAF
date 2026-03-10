# gstaf/forms.py
from django import forms
from .models import Employe, Poste,TacheCarriere

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'poste', 'email', 'date_embauche']
        widgets = {
            'date_embauche': forms.DateInput(attrs={'type': 'date'}),
        }

class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ['titre', 'description', 'departement']
class TacheCarriereForm(forms.ModelForm):
    class Meta:
        model = TacheCarriere
        fields = ['employe', 'type_tache', 'titre', 'description', 'date']
