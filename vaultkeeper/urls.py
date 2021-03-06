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
    url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login', kwargs={'template_name': 'login.html'}),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': 'show vault'}),
    url(r'^vaultkeeper/$', 'vault.views.show_vault', name='show vault'),
    url(r'^vaultkeeper/openvault/$', 'vault.views.open_vault', name='open vault'),
    url(r'^vaultkeeper/vault/new/$', 'vault.views.new_vault', name='new vault'),
    url(r'^vaultkeeper/vault/(?P<id>\d+)/edit/$', 'vault.views.edit_vault', name='edit vault'),
    url(r'^vaultkeeper/vault/(?P<id>\d+)/remove/$', 'vault.views.remove_vault', name='remove vault'),
    url(r'^vaultkeeper/getserial/$', 'vault.views.get_serial', name="get serial"),
    url(r'^vaultkeeper/getcode/$', 'vault.views.get_code', name="get code"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
