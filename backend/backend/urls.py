from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", TemplateView.as_view(template_name='index.html')),
    path("admin/", admin.site.urls),
    path("api/products/", include("products.urls")),
    path("api/users/", include("users.urls")),
]

# Serve static files during development

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()