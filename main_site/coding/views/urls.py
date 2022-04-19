"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:١٨ م
"""
from django.urls import path, include
from .website import urls as website_urls
from .dashboard import urls as dashboard_urls
from .authentication import urls as auth_urls
from .student_platform import urls as student_platform_urls

urlpatterns = [
    path('', include(website_urls)),
    path('dashboard/', include(dashboard_urls)),
    path('auth/', include(auth_urls)),
    path('student-platform/', include(student_platform_urls)),
]
