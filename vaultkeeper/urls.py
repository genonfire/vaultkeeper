from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vaultkeeper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^showvault/', 'vault.views.showVault', name='showVault'),
    url(r'^vault/(?P<id>\d+)/$', 'vault.views.openVault', name='openVault'),
    url(r'^vault/new/$', 'vault.views.newVault', name='newVault'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)