"""
URL configuration for deploy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
#test
from django.contrib import admin
from django.urls import path
from basic.views import home
from basic.views import sample_response,response2,response_json,response_list,response3,querry_per,info,filtering,filterinfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('sample_response/',sample_response),
    path('response2/',response2),
    path('response_json/',response_json),
    path('response_list',response_list),
    path('response3/',response3),
    path('querry_per/',querry_per),
    path('info/',info),
    path('filtering/',filtering),
    path('filterinfo/',filterinfo)
]
