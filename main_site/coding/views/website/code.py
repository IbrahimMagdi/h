"""
    Create by Ahmad Ibrahim
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render
from codes_source.settings import *
from main_site.models import Systems


def website_web(request):
    get_ln = request.GET.get('ln')
    systems = Systems.objects.filter(status=True)
    send_data = {
        'nameSite': nameSite['ar'],
        'systems': systems,
    }
    return render(request, 'website/pages/main.html'.format(get_ln), send_data)
