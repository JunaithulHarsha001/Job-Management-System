from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from . models import Application, Job
from . serializers import ApplicationSerializer, JobSerializer, ApplicationListSerializer, AdminApplicationSerializer, SignupSerializer
from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply_job(request):
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(user = request.user)
            return Response(
                {"detail":"Application submitted successfully"},
                status= status.HTTP_201_CREATED
            )
        except IntegrityError:
            return Response(
                {"detail": "You have already applied to this Job"},
                status= status.HTTP_400_BAD_REQUEST
            )   
    else:
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_jobs(request):
    jobs = Job.objects.filter(is_active=True)
    serializer = JobSerializer(jobs,many= True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_applications(request):
    application = Application.objects.filter(user = request.user)
    serializer = ApplicationListSerializer(application,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_applications(request):
    applications = Application.objects.all()
    serializer = AdminApplicationSerializer(applications,many=True)
    return Response(serializer.data)

@api_view(["PATCH"])
@permission_classes([IsAdminUser])
def admin_update_applications(request,id):
    try:
        application = Application.objects.get(id=id)
    except Application.DoesNotExist:
        return Response(
            {"detail":"Application Does Not Exist"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = AdminApplicationSerializer(application,data = request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Logout authentication
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(
        {"detail": "Logged out successfully"},
        status= status.HTTP_200_OK
    )

#Signup
@api_view(["POST"])
def signup_view(request):
    Serializer = SignupSerializer(data=request.data)
    if Serializer.is_valid():
        return Response(
            {"detail" : "User created Successfully"},
            status= status.HTTP_201_CREATED
        )
    return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)