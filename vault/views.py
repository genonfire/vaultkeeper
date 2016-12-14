from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.conf import settings
from models import Vault
from vault.forms import VaultEditForm
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def show_vault(request):
    vaults = Vault.objects.all().order_by('Type')

    return render(
        request,
        'showvault.html',
        {
            'vaults' : vaults,
            'showType' : 'show',
        }
    )

def open_vault(request):
    vaults = Vault.objects.filter(Type='1account').exclude(Serial='').exclude(Code='')

    return render(
        request,
        'showvault.html',
        {
            'vaults' : vaults,
            'showType' : 'open',
        }
    )

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
            'editType': 'new',
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
            'editType': 'edit',
        }
    )

def remove_vault(request, id):
    vault = get_object_or_404(Vault, pk = id)
    vault.delete()

    return redirect(vault.get_absolute_url())

def get_serial(request):
    id = request.POST.get('id')
    vault = get_object_or_404(Vault, pk = id)

    return HttpResponse(json.dumps(vault.Serial), content_type="application/json")

def get_code(request):
    id = request.POST.get('id')
    pos1 = int(request.POST.get('pos1'))
    pos2 = int(request.POST.get('pos2'))
    vault = get_object_or_404(Vault, pk = id)
    codelist = vault.Code.split(',')
    code1 = int(codelist[pos1]) / 100
    deadcode1 = int(codelist[pos1]) % 100
    deadcode2 = int(codelist[pos2]) / 100
    code2 = int(codelist[pos2]) % 100

    return HttpResponse(json.dumps([code1, deadcode1, deadcode2, code2]), content_type="application/json")