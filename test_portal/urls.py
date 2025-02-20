# test_portal/urls.py
from django.contrib import admin
from django.urls import path, include
from exams.staff_admin import staff_admin_site
from exams.views import StaffRegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff-admin/', staff_admin_site.urls),
    path('api/staff/signup/', StaffRegisterView.as_view(), name='staff-signup'),
    path('staff/signup/', StaffRegisterView.as_view(), name='staff-signup'),
    path('api/', include('exams.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

