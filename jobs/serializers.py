from rest_framework import serializers
from . models import Application
from . models import Job
from django.contrib.auth.models import User

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["job"]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class ApplicationListSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    class Meta:
        model = Application
        fields = ["job","status","applied_at"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]

class AdminApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Application
        fields = ["id","user","job","status","applied_at"]
        read_only_fields = ["user","job","applied_at"]

#signup
class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password"]
    
    def create(self,validated_data):
        user = User.objects.create_user(
            username= validated_data["username"],
            email= validated_data["email"],
            password = validated_data["password"],
        )
        return user


