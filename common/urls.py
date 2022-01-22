from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls

admin.sites.AdminSite.index_title = "Приложения"
admin.site.site_title = 'Знаменитости сериалов'
admin.site.site_header = 'Знаменитости сериалов'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("common.api_urls")),
    path('api/auth_token/', include('djoser.urls.authtoken')),

]
urlpatterns += doc_urls

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
