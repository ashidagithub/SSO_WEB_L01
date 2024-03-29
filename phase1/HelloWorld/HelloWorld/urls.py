"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

'''
import sys
sys.path.append('..')
'''
from .views.view_direct import *
#from HelloWorld.views.view_direct import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vdhello/', vdhello),
    path('vdhtml1/', vdhtml1),
    path('vdhtml2/', vdhtml2),
    path('vdhtml3/', vdhtml3),
    path('index/', index),
]
