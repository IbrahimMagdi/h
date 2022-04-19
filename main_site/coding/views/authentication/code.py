"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render, redirect
from codes_source.settings import *


def login_web(request):
    if not request.user.is_authenticated:
        get_ln = request.GET.get('ln')
        if get_ln == 'ar' or get_ln == 'en':
            get_ln = get_ln
        else:
            get_ln = 'ar'

        send_data = {
            'nameSite': nameSite[get_ln],
        }
        return render(request, 'login.html'.format(get_ln), send_data)
    else:
        if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser:
            return redirect('dashboard_web')
        else:
            return redirect('website')
