from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from .models import Museo
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

import random
import urllib.request
import sys
import operator


# Create your views here.
info_museo = {} #DICCIONARIO
lista_museos = [] #LISTA

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
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['NOMBRE']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['DESCRIPCION-ENTIDAD']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['HORARIO']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['TRANSPORTE']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['ACCESIBILIDAD']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['CONTENT-URL']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['NOMBRE-VIA']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['CLASE-VIAL']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['TIPO-NUM']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['NUM']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['LOCALIDAD']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['PROVINCIA']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['CODIGO-POSTAL']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['BARRIO']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['DISTRITO']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['COORDENADA-X']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['COORDENADA-Y']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['LATITUD']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['LONGITUD']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['TELEFONO']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['FAX']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

        if tag == 'atributo' and self.atrSection in ['EMAIL']:
            info_museo[self.atrSection] = self.theContent
            self.atrSection = ""

            info_museo['COMENTARIO'] = random.randint(0,20)

            nuevo_museo = Museo(entidad=info_museo['ID-ENTIDAD'],
                                nombre=info_museo['NOMBRE'],
                                descripcion=info_museo['DESCRIPCION-ENTIDAD'],
                                horario=info_museo['HORARIO'],
                                transporte=info_museo['TRANSPORTE'],
                                accesibilidad=info_museo['ACCESIBILIDAD'],
                                url=info_museo['CONTENT-URL'],
                                via=info_museo['NOMBRE-VIA'],
                                clase=info_museo['CLASE-VIAL'],
                                tipo=info_museo['TIPO-NUM'],
                                num=info_museo['NUM'],
                                localidad=info_museo['LOCALIDAD'],
                                provincia=info_museo['PROVINCIA'],
                                codigo=info_museo['CODIGO-POSTAL'],
                                barrio=info_museo['BARRIO'],
                                distrito=info_museo['DISTRITO'],
                                coordenadax=info_museo['COORDENADA-X'],
                                coordenaday=info_museo['COORDENADA-Y'],
                                latitud=info_museo['LATITUD'],
                                longitud=info_museo['LONGITUD'],
                                telefono=info_museo['TELEFONO'],
                                fax=info_museo['FAX'],
                                email=info_museo['EMAIL'],
                                comentarios=info_museo['COMENTARIO'])

            nuevo_museo.save()

        if tag == self.dataType:
            lista_museos.append(info_museo)
        if self.inSection:
            self.inSection = 0
            self.AtrSection = ""
            self.theContent = ""

    def characters(self, chars):
        if self.inSection:
            self.theContent = self.theContent + chars


formulario = """
<form action="" method="POST">
    <input type="submit" value="CARGAR MUSEOS">
</form>
"""
dic_comentarios = {}

@csrf_exempt
def principal(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'


    #MUESTRO LA OPCION: MOSTRAR MUSEOS

    if request.method == "POST":
        #DESCARGO XML Y CREO LA BASE DE DATOS
        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        myfile = open('/home/alumnos/nalonso/Documentos/saro/final/X-Serv-Practica-Museos/newproject/museos/xml', 'w')
        xmlFile = urllib.request.urlopen('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')
        theParser.parse(xmlFile)
        print ("Parse complete")

        #MUESTRO LA LISTA DE MUSEOS Y DEPLEGABLE DE 5 EN 5
        lista= Museo.objects.all()
        for museo in lista:
            dic_comentarios[museo.id] = museo.comentarios
        lista_ordenada = sorted(dic_comentarios.items(), key=operator.itemgetter(1))
        grupo = lista_ordenada[0:5]
        m = []
        for i in range(5):
            identificador = grupo[i]
            aux = identificador[0]
            m.append(Museo.objects.get(id=aux))



        c =({'registro' : logged, 'contenido' : "PAGINA PRINCIPAL", 'museos' : m})
        template = get_template("museos/index.html")
        return HttpResponse(template.render(c))

    else:
        c =({'registro' : logged, 'contenido' : "PAGINA PRINCIPAL", 'formulario' : formulario})
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
