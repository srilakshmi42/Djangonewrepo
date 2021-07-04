from django.http import HttpResponse
def showIndex(http_request):
    message='''
    <html>
    <body bgcolor="yellow">
    <h1> welcome to django class</h1>
    </body
    </html>
    '''
    return HttpResponse(message)
