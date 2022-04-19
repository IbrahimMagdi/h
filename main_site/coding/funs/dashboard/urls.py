"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .nationalities import urls as nationalities_urls_fun
from .systems import urls as systems_urls_fun
from .teams import urls as teams_urls_fun
from .students import urls as students_urls_fun

urlpatterns = [
    path('nationalities/', include(nationalities_urls_fun)),
    path('systems/', include(systems_urls_fun)),
    path('teams/', include(teams_urls_fun)),
    path('students/', include(students_urls_fun)),
]