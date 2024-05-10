
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title=" online shop API",
        default_version='v1',
        description="Online shop API",
        terms_of_service="https://www.google.com",
        contact=openapi.Contact(email="nurlanmamitov9404@gmail.com"),
        license=openapi.License(name="demo service"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('category.urls')),
    path('', include('users.urls')),
    path('music/', include('music.urls')),
    path('category/', include('API.urls')),
    path('docs-swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('docs-redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='rodoc'),

]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)