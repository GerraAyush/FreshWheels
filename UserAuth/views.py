from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_home_page(httpRequest):
    return render(httpRequest, 'homePage.html', {})

def get_login(httpRequest):
    return HttpResponse("Login")