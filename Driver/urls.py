from django.urls import path
from . import views

app_name = "Driver"
urlpatterns = [
    path('driversInfo', views.get_driversInfo_page, name="driversInfo"),
]