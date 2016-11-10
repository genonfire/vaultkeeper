from django.shortcuts import render
from django.http import HttpResponse

from models import Vault

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def showVault(request):
    return HttpResponse('Hello World!')

def openVault(request, *args):
    vault = Vault.objects.get(pk = args[0])

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