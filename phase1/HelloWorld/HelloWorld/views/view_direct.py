from django.http import HttpResponse

def vdhello(request):
    return HttpResponse("Hello world ! ")
