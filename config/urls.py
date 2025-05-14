from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="🎵 Musiqa API xujjati",
        default_version='v1',
        description="""
        <b>Assalomu alaykum!</b> 👋<br>
        Ushbu API orqali quyidagi bo‘limlar bilan ishlashingiz mumkin:<br><br>

        • 🎤 <b>San'atkorlar (Artists)</b><br>
        • 💿 <b>Albomlar (Albums)</b><br>
        • 🎧 <b>Qo‘shiqlar (Songs)</b><br>
        • 📂 <b>Pleylistlar (Playlists)</b><br><br>

        <b>Asosiy imkoniyatlar:</b><br>
        ✅ To‘liq CRUD amallar (yaratish, o‘qish, yangilash, o‘chirish)<br>
        ✅ Media yuklash (rasm/audio)<br>
        ✅ Swagger va ReDoc hujjatlari<br>
        ✅ Ochiq va yopiq (login talab qiladigan) endpointlar<br><br>

        <i>Django REST Framework va drf-yasg yordamida ishlab chiqilgan.</i>
        """,
        terms_of_service="https://sizningsaytingiz.uz/shartlar/",
        contact=openapi.Contact(
            name="Texnik yordam",
            email="aloqa@sizningsaytingiz.uz",
            url="https://sizningsaytingiz.uz"
        ),
        license=openapi.License(name="MIT litsenziya"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Asosiy API yo‘llari
    path('api/', include('music.urls')),

    # API hujjatlar
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

# Rasm va media fayllarni ko‘rsatish (faqat DEBUG rejimida)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
