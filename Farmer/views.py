from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import FarmerInfoForm

@login_required
def get_farmersInfo_page(httpRequest):
    if httpRequest.method == "POST":
        form = FarmerInfoForm(httpRequest.POST)
        if form.is_valid():
            farmer_profile = form.save()
            print(farmer_profile)
            httpRequest.user.extendeduser.farmer = farmer_profile
            httpRequest.user.extendeduser.save()
            return redirect('Farmer:profile')
    return render(httpRequest, 'farmersInfo.html', {})

@login_required
def get_profile_page(httpRequest):
    if httpRequest.user.extendeduser.choice != 'Farmer':
        return redirect(f"{httpRequest.user.extendeduser.choice}:profile")
    return render(httpRequest, 'profile.html', {})