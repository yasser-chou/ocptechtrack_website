from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews
msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
