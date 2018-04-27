from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from .models import Museo

# Create your views here.

@csrf_exempt
def principal(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    c =({'registro' : logged, 'contenido' : "PAGINA PRINCIPAL"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))



@csrf_exempt
def usuario(request, usuario):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    c =({'registro' : logged, 'contenido' : "PAGINA DE USUARIO"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))




@csrf_exempt
def museos(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    c =({'registro' : logged, 'contenido' : "LISTA DE MUSEOS"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))




@csrf_exempt
def museo_id(request, identificador):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    c =({'registro' : logged, 'contenido' : "PAGINA INFORMACION DE UN MUSEO"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))




@csrf_exempt
def usuario_xml(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    c =({'registro' : logged, 'contenido' : "USUARIO XML"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))



@csrf_exempt
def about(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    c =({'registro' : logged, 'contenido' : "PAGINA DE INFORMACION"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))
