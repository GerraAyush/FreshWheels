from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerInfoForm

@login_required
def get_customerInfo_page(httpRequest):
    if httpRequest.method == "POST":
        form = CustomerInfoForm(httpRequest.POST)
        if form.is_valid():
            customer_profile = form.save()
            print(customer_profile)
            httpRequest.user.extendeduser.customer = customer_profile
            httpRequest.user.extendeduser.save()
            return redirect('Customer:profile')
    return render(httpRequest, 'customerInfo.html', {})

@login_required
def get_profile_page(httpRequest):
    if httpRequest.user.extendeduser.choice != 'Customer':
        return redirect(f"{httpRequest.user.extendeduser.choice}:profile")
    return render(httpRequest, 'profile.html', {})