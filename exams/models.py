from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    approved = models.BooleanField(default=False)  # Approval flag

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=255, blank=True, null=True)
    option_b = models.CharField(max_length=255, blank=True, null=True)
    option_c = models.CharField(max_length=255, blank=True, null=True)
    option_d = models.CharField(max_length=255, blank=True, null=True)
    correct_option = models.CharField(
        max_length=1,
        help_text="Enter A, B, C, or D",
        blank=True,
        null=True
    )
    approved = models.BooleanField(default=False)  # Approval flag
    # New field for free-response correct answer text
    correct_answer_text = models.TextField(blank=True, null=True)
    # New field for detailed explanation
    explanation = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.course.name}: {self.question_text[:50]}"

class TestSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.end_time and timezone.is_naive(self.end_time):
            self.end_time = timezone.make_aware(self.end_time)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.course.name} - {self.start_time}"
