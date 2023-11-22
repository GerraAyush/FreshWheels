from . import views
from django.urls import path

app_name = "UserAuth"
urlpatterns = [
    path('', views.get_home_page, name="home_page"),
    path('login', views.get_login, name="login"),
]
