from django import urls
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('craigslist_app.urls')),
]