"""
    Create by Ahmad Ibrahim 
    at ١٢‏/٣‏/٢٠٢٢ - ١٢:٣٠ ص
"""
from django.urls import path, include
from main_site.coding.views import urls as views_urls
from main_site.coding.funs import urls as funs_urls

urlpatterns = [
    path('', include(views_urls)),
    path('fun/', include(funs_urls)),
]