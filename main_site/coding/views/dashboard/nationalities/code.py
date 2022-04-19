"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render, redirect
from codes_source.settings import *
from main_site.models import Nationalities
from django.http import Http404


def all_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        items = Nationalities.objects.all()
        send_data = {
            'nameSite': nameSite[get_ln],
            'items': items
        }
        return render(request, 'pages/dashboard/nationalities/all/{}.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')


def add_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        send_data = {
            'nameSite': nameSite[get_ln],
        }
        return render(request, 'pages/dashboard/nationalities/add/{}.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')


def edit_web(request, id):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        try:
            item = Nationalities.objects.get(id=id)
        except:
            item = None
        if item:
            send_data = {
                'nameSite': nameSite[get_ln],
                'item': item,
            }
            return render(request, 'pages/dashboard/nationalities/edit/{}.html'.format(get_ln), send_data)
        else:
            return Http404
    else:
        return redirect('login_web')
