from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Course, Question, TestSession
from django.contrib.auth.models import User  # Using Django's default User model

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        is_new = not change
        super().save_model(request, obj, form, change)
        if is_new:
            subject = f"New Course Available: {obj.name}"
            course_link = "https://petrox-test-frontend.onrender.com"
            message = (
                f"Dear User,\n\n"
                f"We are excited to announce that a new course has been uploaded: {obj.name}.\n"
                f"Check it out here: {course_link}\n\n"
                f"Best regards,\nThe Petrox Team"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = list(User.objects.values_list('email', flat=True))
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'question_text',
        'correct_option',
        'get_correct_answer_text',  # Custom getter method for free-response answer text
        'get_explanation'           # Custom getter method for explanation
    )
    fields = (
        'course',
        'question_text',
        'option_a',
        'option_b',
        'option_c',
        'option_d',
        'correct_option',
        'correct_answer_text',
        'explanation'
    )

    def get_correct_answer_text(self, obj):
        return obj.correct_answer_text or ""
    get_correct_answer_text.short_description = "Correct Answer Text"

    def get_explanation(self, obj):
        return obj.explanation or ""
    get_explanation.short_description = "Explanation"

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TestSession)
