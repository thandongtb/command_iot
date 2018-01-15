from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasScope
from oauth2_provider.views.generic import ScopedProtectedResourceView

scopes = ['api-iot', 'api-iot-data']


class ApiResource(ScopedProtectedResourceView):
    required_scopes = scopes


class ApiResourceRF(viewsets.ViewSet):
    permission_classes = [TokenHasScope]
    required_scopes = scopes
