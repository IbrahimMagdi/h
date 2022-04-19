from django.contrib import admin
from django.urls import path, include

# apps
from main_site.coding import urls as main_site_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_site_urls)),
]
