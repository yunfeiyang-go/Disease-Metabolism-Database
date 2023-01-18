"""D&M URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
 
from . import views
 
urlpatterns = [
    re_path('^Home$', views.home_view, name='Home'),
    re_path(r'^Metabolism/.*$', views.metabolism_view, name='Metabolism'),
    re_path(r'^Disease/.*$', views.disease_view, name='Disease'),
    re_path(r'^Tutorial$', views.tutorial_view, name='Tutorial'),
    re_path(r'^About$', views.about_view, name='About'),
    re_path(r'^kenan$', views.cytoscape_view, name='Cytoscape examples'),
]