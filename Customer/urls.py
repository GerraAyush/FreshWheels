from django.urls import path
from . import views

app_name = "Customer"
urlpatterns = [
    path('info', views.get_customerInfo_page, name="info"),
    path('profile', views.get_profile_page, name="profile"),
]
