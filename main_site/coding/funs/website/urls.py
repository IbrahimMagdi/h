"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .auth.login import login_fun

urlpatterns = [
    path('login', login_fun),
]