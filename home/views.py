from django.http import HttpResponse

def home(request):
    return HttpResponse("김건국, 임효근, 한상민")
