"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .my_profile import urls as my_profile_urls


urlpatterns = [
    path('my-profile', include(my_profile_urls)),
]