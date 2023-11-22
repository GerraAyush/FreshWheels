from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_farmersInfo_page(httpRequest):
    return render(httpRequest, 'farmersInfo.html', {})