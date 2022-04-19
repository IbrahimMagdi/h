"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .code import *

urlpatterns = [
    path('', home_site_web, name='home_site_web'),
]