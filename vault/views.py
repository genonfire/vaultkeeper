from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from models import Vault
from vault.forms import VaultEditForm

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def show_vault(request):
    vaults = Vault.objects.filter()
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
        Logo = vault.Logo.url
        )

    return HttpResponse(textformatted)

def new_vault(request):
    if request.method == "GET":
        newForm = VaultEditForm()
    elif request.method == "POST":
        newForm = VaultEditForm(request.POST, request.FILES)

    if newForm.is_valid():
        newVault = newForm.save()
        return redirect(newVault.get_absolute_url())

    return render(
        request,
        'newvault.html',
        {
            'form': newForm,
        }
    )