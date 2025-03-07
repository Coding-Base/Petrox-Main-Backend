from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Question, TestSession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TestSessionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    duration = serializers.IntegerField()

    class Meta:
        model = TestSession
        fields = ['id', 'user', 'course', 'questions', 'start_time', 'end_time', 'score', 'duration']

# New Staff Registration Serializer
class StaffRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with is_staff=True
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_staff = True
        user.save()
        return user
