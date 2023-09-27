
#Request:: Realizar peticiones
#HttpResponse: Enviar repuesta con protocolo HTTP-

from django.http import HttpResponse


def bienvenida(request):
    return HttpResponse("marcela te amo")