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

num_pagina = 0
formulario = """
    <form action=""" + str(num_pagina) + """ method="POST">
    <input type="submit" value="CARGAR MUSEOS">
</form>
"""


dic_comentarios = {}

@csrf_exempt
def principal(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'


    c =({'registro' : logged, 'contenido' : "Bienvenido a nuestra página.", 'formulario' : formulario})
    template = get_template("museos/index_museo.html")
    return HttpResponse(template.render(c))

@csrf_exempt
def principal_anotada(request, num_pagina):

    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'

    if int(num_pagina) == 0:
        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        xmlFile = urllib.request.urlopen('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')
        theParser.parse(xmlFile)


    #MUESTRO LA LISTA DE MUSEOS Y DEPLEGABLE DE 5 EN 5
    lista= Museo.objects.all()
    for museo in lista:
        dic_comentarios[museo.id] = museo.comentarios

    lista_ordenada = sorted(dic_comentarios.items(), key=operator.itemgetter(1))
    lista_cinco = lista_ordenada[int(num_pagina):int(num_pagina)+5]

    m = []
    via = []
    clase = []
    tipo = []
    num = []
    localidad = []
    provincia = []
    url = []
    codigo = []
    barrio = []
    distrito = []
    lista_id = []
    for i in range(0,5):

        id_tupla = lista_cinco[i]
        id_museo = id_tupla[0]
        lista_id.append(id_museo)
        m.append(Museo.objects.get(id=id_museo))
        nombre = Museo.objects.get(id=id_museo)

        lista= Museo.objects.all()
        for museo in lista:
            if museo.nombre == str(nombre):
                via.append(museo.via)
                clase.append(museo.clase)
                tipo.append(museo.tipo)
                num.append(museo.num)
                localidad.append(museo.localidad)
                provincia.append(museo.provincia)
                codigo.append(museo.codigo)
                barrio.append(museo.barrio)
                distrito.append(museo.distrito)
                url.append(museo.url)


    num_pagina = int(num_pagina) + 5
    formulario_desplegable = """
                                <form action=""" + str(num_pagina) + """ method="POST">
                                <input type="submit" value="VER MAS">
                                </form>
                                """



    info_museo_1 = "<a href=" + str(url[0]) + ">" + str(m[0]) + "</a></br>" + str(clase[0]) + " " + str(via[0]) + " " + str(tipo[0]) + " " + str(num[0]) + " " + str(localidad[0]) + " " + str(provincia[0]) + "</br>" + str(codigo[0]) + " " + str(barrio[0]) + "</br>" + str(distrito[0]) + "</br><a href=" + "/museos/" + str(lista_id[0]) + ">" + "Mas información" + "</a></br>"
    info_museo_2 = "<a href=" + str(url[1]) + ">" + str(m[1]) + "</a></br>" + str(clase[1]) + " " + str(via[1]) + " " + str(tipo[1]) + " " + str(num[1]) + " " + str(localidad[1]) + " " + str(provincia[1]) + "</br>" + str(codigo[1]) + " " + str(barrio[1]) + "</br>" + str(distrito[1]) + "</br><a href=" + "/museos/" + str(lista_id[1]) + ">" + "Mas información" + "</a></br>"
    info_museo_3 = "<a href=" + str(url[2]) + ">" + str(m[2]) + "</a></br>" + str(clase[2]) + " " + str(via[2]) + " " + str(tipo[2]) + " " + str(num[2]) + " " + str(localidad[2]) + " " + str(provincia[2]) + "</br>" + str(codigo[2]) + " " + str(barrio[2]) + "</br>" + str(distrito[2]) + "</br><a href=" + "/museos/" + str(lista_id[2]) + ">" + "Mas información" + "</a></br>"
    info_museo_4 = "<a href=" + str(url[3]) + ">" + str(m[3]) + "</a></br>" + str(clase[3]) + " " + str(via[3]) + " " + str(tipo[3]) + " " + str(num[3]) + " " + str(localidad[3]) + " " + str(provincia[3]) + "</br>" + str(codigo[3]) + " " + str(barrio[3]) + "</br>" + str(distrito[3]) + "</br><a href=" + "/museos/" + str(lista_id[3]) + ">" + "Mas información" + "</a></br>"
    info_museo_5 = "<a href=" + str(url[4]) + ">" + str(m[4]) + "</a></br>" + str(clase[4]) + " " + str(via[4]) + " " + str(tipo[4]) + " " + str(num[4]) + " " + str(localidad[4]) + " " + str(provincia[4]) + "</br>" + str(codigo[4]) + " " + str(barrio[4]) + "</br>" + str(distrito[4]) + "</br><a href=" + "/museos/" + str(lista_id[4]) + ">" + "Mas información" + "</a></br>"

    c =({'registro' : logged, 'contenido' : "PAGINA PRINCIPAL", 'museo1' : info_museo_1, 'museo2' : info_museo_2, 'museo3' : info_museo_3, 'museo4' : info_museo_4,'museo5' : info_museo_5, 'desplegable': formulario_desplegable})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))


@csrf_exempt
def usuario(request, usuario):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'

    c =({'registro' : logged, 'contenido' : "PAGINA DE USUARIO"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))


@csrf_exempt
def museos(request):

    formulario_filtro = """
                        <form action="" method="POST">
                        Buscar por distrito: <input type="text" name="distrito"><br>
                        <input type="submit" value="VER">
                        </form>
                        """

    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'

    if request.method == "POST":

        distrito = request.POST['distrito']

        informacion = "LISTA DE MUSEOS EN EL DISTRITO SELECCIONADO: </br></br>"
        lista = Museo.objects.all()
        exist = False
        for museo in lista:
            if museo.distrito == distrito:
                exist = True
                informacion += str(museo.nombre) + ": <a href=" + str(museo.url)+ ">Acceder al museo</a><br>"

        if exist == False:
            informacion = "EL DISTRITO SELECCIONADO NO EXISTE."

        c =({'registro' : logged, 'lista_museos': informacion})
        template = get_template("museos/index_museo.html")
        return HttpResponse(template.render(c))

    else:

        informacion = "LISTA DE MUSEOS</br></br>"
        lista = Museo.objects.all()
        for museo in lista:
            informacion += str(museo.nombre) + ": <a href=" + str(museo.url)+ ">Acceder al museo</a><br>"

        c =({'formulario_filtro': formulario_filtro, 'registro' : logged, 'lista_museos': informacion})
        template = get_template("museos/index_museo.html")
        return HttpResponse(template.render(c))


@csrf_exempt
def museo_id(request, identificador):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br><a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'

    nombre = Museo.objects.get(id=identificador)
    lista = Museo.objects.all()
    for museo in lista:
        if museo.nombre == str(nombre):
            if museo.accesibilidad == 0:
                accesibilidad = "El museo es accesible. "
            else:
                accesibilidad = "El museo no es accesible. "
            informacion = museo.nombre + "</br></br>" + museo.descripcion + "</br></br>" + museo.transporte + "</br></br>" + accesibilidad + "</br></br>" +  "<a href=" + str(museo.url) + ">Ver museo</a>" + "</br></br>Dirección: </br>" + museo.clase + " " + museo.via + "</br>" + museo.localidad + "</br>" + museo.provincia + "</br>" + museo.codigo + "</br></br>" + "Barrio: " + museo.barrio + "</br>" + "Distrito: " + museo.distrito + "</br></br>Datos de contacto: </br>" + "Teléfono: " + museo.telefono + "</br>" + "Fax: " + museo.fax + "</br>Email: " + museo.email


    c =({'registro' : logged, 'contenido' : "INFORMACION DEL MUSEO</br>" + informacion})
    template = get_template("museos/index_museo.html")
    return HttpResponse(template.render(c))


@csrf_exempt
def usuario_xml(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'

    c =({'registro' : logged, 'contenido' : "USUARIO XML"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))


@csrf_exempt
def about(request):
    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>' + '<a href= "/login">Login</a> <br>'

    c =({'registro' : logged, 'contenido' : "PAGINA DE INFORMACION"})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))
