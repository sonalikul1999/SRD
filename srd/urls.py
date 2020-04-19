from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('aboutus/',aboutus),
    path('service/',service),
    path('portfolio/',portfolio),
    path('blog/',blog),
    path('contact/',contact),
]
