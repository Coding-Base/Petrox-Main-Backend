from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Course, Question, TestSession
from django.contrib.auth.models import User  # Using Django's default User model

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        # Determine if this is a new course
        is_new = not change
        super().save_model(request, obj, form, change)
        if is_new:
            subject = f"New Course Available: {obj.name}"
            # Updated course_link without including a course ID.
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
        'get_correct_answer_text',  # Custom method for free-response correct answer
        'get_explanation'           # Custom method for detailed explanation
    )
    # If your model doesn't yet include the new fields, keep them out of 'fields'.
    # When you add the fields to your model and run migrations, you can add them here.
    fields = ('course', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')

    def get_correct_answer_text(self, obj):
        # Return the value of correct_answer_text if it exists; otherwise an empty string.
        return getattr(obj, 'correct_answer_text', '')
    get_correct_answer_text.short_description = "Correct Answer Text"

    def get_explanation(self, obj):
        # Return the value of explanation if it exists; otherwise an empty string.
        return getattr(obj, 'explanation', '')
    get_explanation.short_description = "Explanation"

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TestSession)

