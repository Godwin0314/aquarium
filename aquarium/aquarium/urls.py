"""aquarium URL Configuration

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
from django.contrib import admin
from django.urls import path
from fishmain import views as V1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',V1.fishmain, name="home"),
    path('betta_fish/',V1.betta_fish,name="bfish"),
    path('gourami_fish/',V1.gourami_fish,name="gourami_fish"),
    path('neon_tetra/',V1.neon_tetra,name="neon"),
    path('clown_fish/',V1.clown_fish,name="clown"),
]
