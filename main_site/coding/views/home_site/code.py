"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render
from codes_source.settings import *


def home_site_web(request):
    get_ln = request.GET.get('ln')
    if get_ln == 'ar' or get_ln == 'en':
        get_ln = get_ln
    else:
        get_ln = 'ar'
    send_data = {
        'nameSite': nameSite['ar'],
    }
    return render(request, 'pages/dashboard/main/{}.html'.format(get_ln), send_data)

