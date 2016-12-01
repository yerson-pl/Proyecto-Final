from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/auths/', include('americas_service_apps.auths_api.urls')),
    url(r'^api/catalogo/', include('americas_service_apps.catalogo_api.urls')),
    url(r'^api/asociacion/',
        include('americas_service_apps.asociacion_api.urls')),
    url(r'^api/eventos/',
        include('americas_service_apps.eventos_api.urls')),
]
