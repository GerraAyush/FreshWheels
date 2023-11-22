from django.urls import path
from . import views

app_name = "Farmer"
urlpatterns = [
    path('farmersInfo', views.get_farmersInfo_page, name="farmersInfo"),
]