# gstaf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe, Poste
from .forms import EmployeForm, PosteForm
from .models import TacheCarriere
from .forms import TacheCarriereForm
def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'gstaf/liste_employes.html', {'employes': employes})

def ajouter_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_employes')
    else:
        form = EmployeForm()
    return render(request, 'gstaf/ajouter_employe.html', {'form': form}) 
def modifier_employe(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('liste_employes')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'gstaf/modifier_employe.html', {'form': form})
# Supprimer un employé
def supprimer_employe(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('liste_employes')
    return render(request, 'gstaf/supprimer_employe.html', {'employe': employe})
    # Liste des postes
def liste_postes(request):
    postes = Poste.objects.all()
    return render(request, 'gstaf/liste_postes.html', {'postes': postes})
# Ajouter un poste
def ajouter_poste(request):
    if request.method == 'POST':
        form = PosteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_postes')
    else:
        form = PosteForm()
    return render(request, 'gstaf/ajouter_poste.html', {'form': form})

# Modifier un poste
def modifier_poste(request, pk):
    poste = get_object_or_404(Poste, pk=pk)
    if request.method == 'POST':
        form = PosteForm(request.POST, instance=poste)
        if form.is_valid():
            form.save()
            return redirect('liste_postes')
    else:
        form = PosteForm(instance=poste)
    return render(request, 'gstaf/modifier_poste.html', {'form': form})

# Supprimer un poste
def supprimer_poste(request, pk):
    poste = get_object_or_404(Poste, pk=pk)
    if request.method == 'POST':
        poste.delete()
        return redirect('liste_postes')
    return render(request, 'gstaf/supprimer_poste.html', {'poste': poste})
def home(request):
    return render(request, 'gstaf/home.html')
def liste_taches_carriere(request):
    taches = TacheCarriere.objects.all()
    return render(request, 'gstaf/liste_taches_carriere.html', {'taches': taches})

def ajouter_tache_carriere(request):
    if request.method == 'POST':
        form = TacheCarriereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_taches_carriere')
    else:
        form = TacheCarriereForm()
    return render(request, 'gstaf/ajouter_tache_carriere.html', {'form': form})