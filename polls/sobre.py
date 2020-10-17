from django.http import HttpResponse

def index(request):
    print("Equipe")
    return HttpResponse("Silas!")