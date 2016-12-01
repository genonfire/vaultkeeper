# from __future__ import unicode_literals
from django import forms
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from django.conf import settings

from vault.models import Vault

class RadioSelectWithImageInput(forms.widgets.RadioInput):
    def __unicode__(self):
        if 'id' in self.attrs:
            label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
        else:
            label_for = ''

        if (self.tag().count('value="')) > 0:
            tag = force_unicode(self.tag())
            valueStart = tag.find('value="') + len('value="')
            valueEnd = valueStart + tag[valueStart:].find('"')
            value = tag[valueStart:valueEnd]
        else:
            value = 'logos/item_icon_default.png'
        if len(value) < 4:
            value = 'logos/item_icon_default.png'

        choice_label = conditional_escape(force_unicode(self.choice_label))
        return mark_safe(u'%s<label%s><img src="%s%s"/> %s</label>' % (self.tag(), label_for, settings.STATIC_URL, value, choice_label))

class RadioSelectWithImage(forms.RadioSelect.renderer):
    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield RadioSelectWithImageInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        return RadioSelectWithImageInput(self.name, self.value, self.attrs.copy(), self.choices[idx], idx)

    def render(self):
        return(mark_safe(u'\n'.join([u'<br>%s' % force_unicode(w) for w in self])))

class VaultEditForm(forms.ModelForm):
    class Meta:
        model = Vault
        # exclude = ('Logo', )

        widgets = {
            'Logo' : forms.RadioSelect(renderer=RadioSelectWithImage),
        }
