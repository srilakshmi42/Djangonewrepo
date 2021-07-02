from django.http import HttpResponse
def showIndex(http_request):
    message="Welcome to Django"
    return HttpResponse(message)
