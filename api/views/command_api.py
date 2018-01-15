import requests
from django.http import JsonResponse
from api.views.api_resource import ApiResource
from api.views.command_recognition import CommandRecognition

class PostCommandRecognition(ApiResource):
    def post(self, request):
        try:
            command = request.POST.get('command')
            recognizer = CommandRecognition(sentence=command)
            data = recognizer.detect_iot_commands()
        except:
            return JsonResponse({'error': 'Something went wrong'}, status=400)

        return JsonResponse(data, safe=False)