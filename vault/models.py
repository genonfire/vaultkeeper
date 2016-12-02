#-*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django import forms

# Create your models here.
class Vault(models.Model):
    TYPE_OPTIONS = (
        ('card', '카드'),
        ('account', '계좌'),
        ('membership', '멤버십'),
        ('etc', '기타'),
    )

    LOGO_OPTIONS = (
        ('logos/samsungcard.png', '샘숭카드'),
        ('logos/kdb.png', '산업은행'),
        ('logos/shinhan.png', '신한은행'),
        ('logos/keb.png', '외환은행'),
        ('logos/woori.png', '우리은행'),
    )

    Type = models.CharField(max_length=20, choices=TYPE_OPTIONS, default='card')
    Name = models.CharField(max_length=30)
    Number = models.CharField(max_length=50)
    Valid = models.CharField(max_length=20, blank=True)
    CVC = models.CharField(max_length=10, blank=True)
    Logo = models.CharField(max_length=50, choices=LOGO_OPTIONS, blank=True)

    def delete(self, *args, **kwargs):
        self.Logo.delete();
        super(Vault, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('open vault', kwargs={'id': self.id})
