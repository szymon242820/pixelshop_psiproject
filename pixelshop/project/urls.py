"""pixelshop URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Django
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include
from django.urls import path

# 3rd-party
from decorator_include import decorator_include

# Project
from pixelshop.views import HomePageView

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
        ),
    path(
        'pixelshop/',
        include('pixelshop.urls'),
        ),
    path(
        'api/',
        decorator_include(
            staff_member_required,
            'api.urls',
            ),
        ),
    path(
        '',
        HomePageView.as_view(),
        name='homepage',
        ),
]
