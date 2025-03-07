from django.urls import path
from .views import (
    TestSessionDetailAPIView,
    CourseListAPIView, 
    AddQuestionAPIView,
    StartTestAPIView, 
    SubmitTestAPIView, 
    TestHistoryAPIView,
    RegisterUserAPIView,  # Registration view for normal users
    StaffRegisterView     # New registration view for staff accounts
)

urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('admin/add-question/', AddQuestionAPIView.as_view(), name='add-question'),
    path('start-test/', StartTestAPIView.as_view(), name='start-test'),
    path('submit-test/<int:session_id>/', SubmitTestAPIView.as_view(), name='submit-test'),
    path('history/', TestHistoryAPIView.as_view(), name='test-history'),
    path('users/', RegisterUserAPIView.as_view(), name='register-user'),
    path('staff/signup/', StaffRegisterView.as_view(), name='staff-signup'),
    path('test-session/<int:id>/', TestSessionDetailAPIView.as_view(), name='test-session-detail'),
]
