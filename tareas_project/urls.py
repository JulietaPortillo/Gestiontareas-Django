from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from myapp import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include("myapp.urls"))
]