from json import loads

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import *
from .utils import *

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'brightbytes/index.html')

def login_view(request):
    if request.method == 'POST':
        data = loads(request.body)

        user = authenticate(
            request, 
            username=data.get('username', ''), 
            password=data.get('password', '')
        )

        if user is None:
            return JsonResponse({'error_type': 'login'}, status=400)

        login(request, user)
        return JsonResponse({}, status=200)

    else:
        return render(request, 'brightbytes/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('brightbytes:index'))

def register(request):
    if request.method == 'POST':
        data = loads(request.body)
        password = data.get('password', '')
        username = data.get('username', '')

        # Ensure form data is not empty
        for val in data.values():
            if not val:
                return JsonResponse({'error_type': 'empty'}, status=400)

        # Validate password
        if not (check_upper(password) and check_lower(password) and check_digit(password)):
            return JsonResponse({'error_type': 'password_invalid'}, status=400)

        # Ensure that password is the same as confirm-password
        if password != data.get('confirm-password', ''):
            return JsonResponse({'error_type': 'confirm_invalid'}, status=400)

        if User.objects.filter(email=data.get('email', '')).exists():
            return JsonResponse({'error_type': 'mail_taken'}, status=409)

        try:
            user = User.objects.create_user(
                first_name=data.get('firstname', '').capitalize(),
                last_name=data.get('lastname', '').capitalize(),
                username=data.get('username', '').lower(),
                email=data.get('email', ''),
                password=password,
            )
            user.save()
            login(request, user)

        except IntegrityError:
            return JsonResponse({'error_type': 'username_taken'}, status=409)

        request.session['username'] = username

        return JsonResponse({}, status=200)

    else:
        return render(request, 'brightbytes/register.html')
