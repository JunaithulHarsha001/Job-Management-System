from django.urls import path
from . import views

#user API
urlpatterns = [
    path("",views.get_jobs,name="jobs_list"),
    path("apply/",views.apply_job,name = "apply_job"),
    path("my_applications/",views.get_applications,name= "user_applications"),

    #admin API
    path("admin/applications/",views.admin_applications,name= "admin_applications"),
    path("admin/applications/<int:id>/",views.admin_update_applications,name = "admin_update_application"),

    #auth API
    path("logout/",views.logout_view,name= "logout")
]