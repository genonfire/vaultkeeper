#-*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django import forms
from django.conf import settings
from fernet_fields import EncryptedCharField, EncryptedTextField

class Vault(models.Model):
    TYPE_OPTIONS = (
        ('1account', '계좌'),
        ('2card', '카드'),
        ('3membership', '멤버십'),
        ('4etc', '기타'),
    )

    LOGO_OPTIONS = (
        ('logos/kdb.png', '산업은행'),
        ('logos/keb.png', '외환은행'),
        ('logos/woori.png', '우리은행'),
        ('logos/shinhan.png', '신한은행'),
        ('logos/kfcc.png', '새마을금고'),
        ('logos/kiwoom.png', '키움증권'),
        ('logos/samsungfn.png', '삼성증권'),
        ('logos/samsungcard.png', '삼성카드'),
        ('logos/koreanair.png', '대한항공'),
        ('logos/asiana.png', '아시아나'),
        ('logos/asiamiles.png', '아시아마일스'),
        ('logos/finnair.png', '핀에어'),
        ('logos/spg.png', 'SPG'),
        ('logos/hertz.png', 'Hertz'),
        ('logos/hyatt.png', 'HYATT'),
        ('logos/marriot.png', '매리어트'),
        ('logos/gs.png', 'GS'),
        ('logos/homeplus.png', '홈플러스'),
        ('logos/okcashbag.png', 'OK 캐쉬백'),
        ('logos/skt.png', 'SKT'),
        ('logos/olleh.png', '올레'),
    )

    User = models.ForeignKey(settings.AUTH_USER_MODEL)
    Type = models.CharField(max_length=20, choices=TYPE_OPTIONS, default='1account')
    Name = EncryptedCharField(max_length=20)
    Number = EncryptedCharField(max_length=50)
    Valid = EncryptedCharField(max_length=20, blank=True)
    CVC = EncryptedCharField(max_length=10, blank=True)
    Logo = models.CharField(max_length=50, choices=LOGO_OPTIONS, blank=True)
    Serial = EncryptedCharField(max_length=20, blank=True)
    Code = EncryptedTextField(blank=True)

    def get_absolute_url(self):
        return reverse_lazy('show vault')
