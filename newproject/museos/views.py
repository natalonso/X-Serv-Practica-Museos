from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from .models import Museo

import urllib.request
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

# Create your views here.
lista_museos = {} #DICCIONARIO
museo = [] #LISTA

class myContentHandler(ContentHandler):

    def __init__(self):
        self.dataType = 'contenido'
        self.inContent = True
        self.theContent = ""
        self.inSection = False
        self.atrSection = ''


    def startElement(self,tag,attrs):
        if tag == "atributo" and attrs["nombre"] in ['ID-ENTIDAD', 'NOMBRE', 'DESCRIPCION-ENTIDAD','HORARIO',
                                                     'TRANSPORTE','ACCESIBILIDAD','CONTENT-URL',
                                                     'NOMBRE-VIA','CLASE-VIAL','TIPO-NUM', 'NUM',
                                                     'LOCALIDAD', 'PROVINCIA', 'CODIGO-POSTAL', 'BARRIO', 'DISTRITO',
                                                     'COORDENADA-X','COORDENADA-Y','LATITUD','LONGITUD',
                                                     'TELEFONO','FAX','EMAIL']:
            self.atrSection = attrs['nombre']
            self.inSection = 1

    def endElement(self, tag):
        if tag == 'atributo' and self.atrSection in ['ID-ENTIDAD']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['NOMBRE']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['DESCRIPCION-ENTIDAD']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['HORARIO']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['TRANSPORTE']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['ACCESIBILIDAD']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['CONTENT-URL']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['NOMBRE-VIA']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['CLASE-VIAL']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['TIPO-NUM']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['NUM']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['LOCALIDAD']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['PROVINCIA']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['CODIGO-POSTAL']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['BARRIO']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['DISTRITO']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['COORDENADA-X']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['COORDENADA-Y']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['LATITUD']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['LONGITUD']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['TELEFONO']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['FAX']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['EMAIL']:
            lista_museos[self.atrSection] = self.theContent
            self.atrSection = ""



            nuevo_museo = Museo(entidad=lista_museos['ID-ENTIDAD'],
                                nombre=lista_museos['NOMBRE'],
                                descripcion=lista_museos['DESCRIPCION-ENTIDAD'],
                                horario=lista_museos['HORARIO'],
                                transporte=lista_museos['TRANSPORTE'],
                                accesibilidad=lista_museos['ACCESIBILIDAD'],
                                url=lista_museos['CONTENT-URL'],
                                via=lista_museos['NOMBRE-VIA'],
                                clase=lista_museos['CLASE-VIAL'],
                                tipo=lista_museos['TIPO-NUM'],
                                num=lista_museos['NUM'],
                                localidad=lista_museos['LOCALIDAD'],
                                provincia=lista_museos['PROVINCIA'],
                                codigo=lista_museos['CODIGO-POSTAL'],
                                barrio=lista_museos['BARRIO'],
                                distrito=lista_museos['DISTRITO'],
                                coordenadax=lista_museos['COORDENADA-X'],
                                coordenaday=lista_museos['COORDENADA-Y'],
                                latitud=lista_museos['LATITUD'],
                                longitud=lista_museos['LONGITUD'],
                                telefono=lista_museos['TELEFONO'],
                                fax=lista_museos['FAX'],
                                email=lista_museos['EMAIL'])

            nuevo_museo.save()

        if tag == self.dataType:
            museo.append(lista_museos)
        if self.inSection:
            self.inSection = 0
            self.AtrSection = ""
            self.theContent = ""

    def characters(self, chars):
        if self.inSection:
            self.theContent = self.theContent + chars


@csrf_exempt
def principal(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    #DESCARGO XML Y CREO LA BASE DE DATOS

    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)

    myfile = open('/home/alumnos/nalonso/Documentos/saro/final/X-Serv-Practica-Museos/newproject/museos/xml', 'w')

    xmlFile = urllib.request.urlopen('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')
    theParser.parse(xmlFile)


    print ("Parse complete")

    #MUESTRO LA LISTA DE MUSEOS Y DEPLEGABLE DE 5 EN 5

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
