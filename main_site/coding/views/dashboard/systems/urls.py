"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .code import *

urlpatterns = [
    path('all', all_web, name='systems_all_web'),
    path('add', add_web, name='systems_add_web'),
    path('edit/<int:id>', edit_web, name='systems_edit_web'),
]