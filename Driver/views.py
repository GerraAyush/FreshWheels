from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_driversInfo_page(httpRequest):
    return render(httpRequest, 'driversInfo.html', {})