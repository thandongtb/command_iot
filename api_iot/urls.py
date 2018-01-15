"""api_iot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from api.views.command_api import PostCommandRecognition
from google_site_verification import GOOGLE_SITE_VERIFICATION_URL

router = routers.DefaultRouter()

internal_api = [
    url(r'^post/detect_command', csrf_exempt(PostCommandRecognition.as_view())),
]

urlpatterns = [
    url(r'^$', include('landing_page.urls')),
    GOOGLE_SITE_VERIFICATION_URL,
    url(r'^admin/', admin.site.urls),
    url(r'^oauth/', include('oauth2_provider.urls', namespace="oauth2_provider")),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(internal_api)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
