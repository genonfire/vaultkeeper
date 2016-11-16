# from __future__ import unicode_literals
from django import forms
from vault.models import Vault

class VaultEditForm(forms.ModelForm):
    class Meta:
        model = Vault