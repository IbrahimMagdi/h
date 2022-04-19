"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .code import *

urlpatterns = [
    path('add', add_fun),
    path('edit', edit_fun),
    path('get-teams', get_team_fun),
]