"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .dashboard import urls as dashboard_urls_fun
from .website import urls as website_urls_fun

urlpatterns = [
    path('dashboard/', include(dashboard_urls_fun)),
    path('website/', include(website_urls_fun)),
]