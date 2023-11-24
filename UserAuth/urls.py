from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "UserAuth"
urlpatterns = [
    path('', views.get_home_page, name="home_page"),
    path('register', views.get_register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='homePage.html'), name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
