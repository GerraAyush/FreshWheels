from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegistrationForm

# Function-Based View for home_page
def get_home_page(httpRequest):
    return render(httpRequest, 'homePage.html', {})

# Function-Based View for registration_page
def get_register(httpRequest):
    if httpRequest.method == "POST":
        form = RegistrationForm(httpRequest.POST)
        print(httpRequest.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            print(form.cleaned_data)
            messages.success(httpRequest, f"Welcome {form.cleaned_data['username']}, your account was created successfully!")
            return redirect('/login')
        else:
            print(form.errors)
            return render(httpRequest, 'login.html', {'form_data': form.cleaned_data, 'errors': form.errors})
    return render(httpRequest, 'login.html', {})