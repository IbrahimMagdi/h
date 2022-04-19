"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .code import *


urlpatterns = [
    path('', my_profile_web, name='my-profile')
]