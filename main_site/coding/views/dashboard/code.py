"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render, redirect
from codes_source.settings import *


def dashboard_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        if get_ln == 'ar' or get_ln == 'en':
            get_ln = get_ln
        else:
            get_ln = 'ar'
        send_data = {
            'nameSite': nameSite['ar'],
        }
        return render(request, 'include_static/{}/index.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')