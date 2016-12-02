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
    url(r'^$', 'vault.views.show_vault', name='show vault'),
    url(r'^vault/(?P<id>\d+)/$', 'vault.views.open_vault', name='open vault'),
    url(r'^vault/new/$', 'vault.views.new_vault', name='new vault'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
