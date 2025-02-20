from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from exams.staff_admin import staff_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),            # Main superuser admin panel
    path('staff-admin/', staff_admin_site.urls),  # Staff admin panel for staff users
    path('api/', include('exams.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
