from django.shortcuts import render

from django.http import HttpResponse
def wish(http_request):
    message="Hello Django Students"
    return HttpResponse(message)
