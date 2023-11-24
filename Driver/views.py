from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DriverInfoForm

@login_required
def get_driversInfo_page(httpRequest):
    if httpRequest.method == "POST":
        form = DriverInfoForm(httpRequest.POST)
        if form.is_valid():
            driver_profile = form.save()
            print(driver_profile)
            httpRequest.user.extendeduser.driver = driver_profile
            httpRequest.user.extendeduser.save()
            return redirect('Driver:profile')
    return render(httpRequest, 'driversInfo.html', {})

@login_required
def get_profile_page(httpRequest):
    if httpRequest.user.extendeduser.choice != 'Driver':
        return redirect(f"{httpRequest.user.extendeduser.choice}:profile")
    return render(httpRequest, 'profile.html', {})