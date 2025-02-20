from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Course, Question
from django.contrib.auth.models import User

class StaffAdminSite(AdminSite):
    site_header = "Petrox Staff Administration"
    site_title = "Staff Admin Portal"
    index_title = "Welcome to the Staff Admin Panel"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

staff_admin_site = StaffAdminSite(name='staff_admin')

class StaffCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved')
    fields = ('name',)  # Staff create a course by providing its name; approved is set automatically.

    def save_model(self, request, obj, form, change):
        if not change:
            obj.approved = False  # Force new courses to be unapproved.
        super().save_model(request, obj, form, change)

class StaffQuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'question_text', 'correct_option', 'correct_answer_text', 'explanation')
    fields = ('course', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'correct_answer_text', 'explanation')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.approved = False  # Force new questions to be unapproved.
        super().save_model(request, obj, form, change)

staff_admin_site.register(Course, StaffCourseAdmin)
staff_admin_site.register(Question, StaffQuestionAdmin)
