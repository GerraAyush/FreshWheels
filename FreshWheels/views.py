from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile(httpRequest):
    if httpRequest.user.extendeduser.choice == 'Farmer':
        if httpRequest.user.extendeduser.farmer == None:
            return redirect('Farmer:info')
        else:
            return redirect('Farmer:profile')
        
    elif httpRequest.user.extendeduser.choice == 'Driver':
        if httpRequest.user.extendeduser.driver == None:
            return redirect('Driver:info')
        else:
            return redirect('Driver:profile')
        
    else:
        if httpRequest.user.extendeduser.customer == None:
            return redirect('Customer:info')
        else:
            return redirect('Customer:profile')