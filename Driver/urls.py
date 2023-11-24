from django.urls import path
from . import views

app_name = "Driver"
urlpatterns = [
    path('info', views.get_driversInfo_page, name="info"),
    path('profile', views.get_profile_page, name="profile"),
]