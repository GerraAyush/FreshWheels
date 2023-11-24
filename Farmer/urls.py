from django.urls import path
from . import views

app_name = "Farmer"
urlpatterns = [
    path('info', views.get_farmersInfo_page, name="info"),
    path('profile', views.get_profile_page, name="profile"),
]