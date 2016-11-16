from django.db import models
from django.core.urlresolvers import reverse_lazy

# Create your models here.
class Vault(models.Model):
    Type = models.CharField(max_length=20)
    Name = models.CharField(max_length=30)
    Number = models.CharField(max_length=50)
    Valid = models.CharField(max_length=20, blank=True)
    CVC = models.CharField(max_length=10, blank=True)
    Logo = models.ImageField(upload_to="images/", blank=True)

    def delete(self, *args, **kwargs):
        self.Logo.delete();
        super(Vault, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('openVault', kwargs={'id': self.id})