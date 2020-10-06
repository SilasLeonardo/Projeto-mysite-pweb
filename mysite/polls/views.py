from django.http import HttpResponse

def index(request):
    print("Minha primira view!")
    return HttpResponse("Hello, World!")