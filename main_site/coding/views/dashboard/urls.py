"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .code import *
from .nationalities import urls as nationalities_urls
from .systems import urls as systems_urls
from .teams import urls as teams_urls
from .students import urls as students_urls

urlpatterns = [
    path('', dashboard_web, name='dashboard_web'),
    path('nationalities/', include(nationalities_urls)),
    path('systems/', include(systems_urls)),
    path('teams/', include(teams_urls)),
    path('students/', include(students_urls)),
]