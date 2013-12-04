from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from userreg.models import RegisteredUser
from userreg.forms import RegisterUserForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def register(request):
    if request.method == 'POST':
        registered_user = RegisteredUser(ip=get_client_ip(request))
        form = RegisterUserForm(request.POST, instance=registered_user)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegisterUserForm()

    return render(request, 'userreg/register.html', {'form': form})

def registration_success(request):
    return render(request, 'userreg/registration_success.html')

