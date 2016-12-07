from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.conf import settings
from models import Vault
from vault.forms import VaultEditForm

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def show_vault(request):
    vaults = Vault.objects.filter().order_by('Type')

    return render(
        request,
        'showvault.html',
        {
            'vaults' : vaults,
        }
    )

def open_vault(request, id):
    vault = get_object_or_404(Vault, pk = id)

    outputText = 'Type: {Type}<br>'
    outputText += 'Name: {Name}<br>'
    outputText += 'Number: {Number}<br>'
    outputText += 'Valid: {Valid}<br>'
    outputText += 'CVC: {CVC}<br>'
    outputText += 'Image: <img src={Logo}><br>'

    textformatted = outputText.format(
        Type = vault.Type,
        Name = vault.Name,
        Number = vault.Number,
        Valid = vault.Valid,
        CVC = vault.CVC,
        Logo = settings.STATIC_URL + vault.Logo
        )

    return HttpResponse(textformatted)

def new_vault(request):
    if request.method == "POST":
        newForm = VaultEditForm(request.POST, request.FILES)
        if newForm.is_valid():
            newVault = newForm.save()
            return redirect(newVault.get_absolute_url())
    elif request.method == "GET":
        newForm = VaultEditForm()

    return render(
        request,
        'editvault.html',
        {
            'form': newForm,
        }
    )

def edit_vault(request, id):
    vault = get_object_or_404(Vault, pk = id)

    if request.method == "POST":
        editForm = VaultEditForm(request.POST, request.FILES, instance=vault)
        if editForm.is_valid():
            editVault = editForm.save()
            return redirect(editVault.get_absolute_url())
    elif request.method == "GET":
        editForm = VaultEditForm(instance=vault)

    return render(
        request,
        'editvault.html',
        {
            'form': editForm,
            'vault': vault,
        }
    )

def remove_vault(request, id):
    vault = get_object_or_404(Vault, pk = id)
    vault.delete()

    return redirect(vault.get_absolute_url())