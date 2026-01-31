from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    #title
    title = models.CharField(max_length = 200)
    #description
    description = models.TextField()
    #company_name
    company_name = models.CharField(max_length= 100)
    #location
    location = models.CharField(max_length = 100)
    #created_at
    created_at = models.DateTimeField(auto_now_add=True)
    #is_active
    is_active = models.BooleanField(default=True)
# Create your models here.

STATUS_CHOICES = (
    ("applied","Applied"),
    ("rejected","Rejected"),
    ("shortlisted","Shortlisted"),
)
class Application(models.Model):
    #user
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #job
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    #status
    status = models.CharField(default= "applied", max_length=100,choices=STATUS_CHOICES)
    #applied_at
    applied_at = models.DateTimeField(auto_now_add=True)
    
    #composite unique constraint (user,job) which is once
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user","job"],
                name= "unique_user_job"
            )
        ]