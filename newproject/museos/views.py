from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from .models import Museo
from .models import Comentario
from .models import Museo_Usuario
from .models import Usuario
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from django.contrib import admin
from django.contrib.auth.models import User


import datetime
import urllib.request
import sys
import operator


# Create your views here.
info_museo = {} #DICCIONARIO
lista_museos = [] #LISTA
dic_comentarios = {}

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

            info_museo['COMENTARIO'] = 0

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


@csrf_exempt
def principal(request):


    num_pagina = 0
    formulario = """
    <div class="box_main">
        <form action=""" + str(num_pagina) + """ method="POST">
        <input class="button" type="submit" value="CARGAR MUSEOS">
    </form>
    </div>
    """


    formulario_filtro_accesibilidad = """
                    <form action="" method="POST">
                    <input class="button log-out" type="submit" value="Buscar los museos accesibles">
                    </form>
                    """

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
        logged = 'Logged in as: ' + request.user.username + '<br> <a class="button log-out" href= "/logout">Logout</a> <br>'
        lista_usuarios = Usuario.objects.all()
        encontrado = False
        for usuario in lista_usuarios:
            if usuario.usuario == request.user.username:
                titulo = usuario.titulo
                color = usuario.color
                tamaño = usuario.tamaño
                encontrado = True
        if encontrado == False:
                titulo = ""
                color = ""
                tamaño = ""
    else:
        enlace_mipagina = ""
        logged = 'Not logged in. <br>' + '<a class="button log-out" href= "/login">Login</a> <br>'
        titulo = ""
        color = ""
        tamaño = ""

    if request.method == "POST":

        informacion = "LISTA DE MUSEOS ACCESIBLES: </br></br>"
        lista = Museo.objects.all()
        for museo in lista:
            if int(museo.accesibilidad) == 1:
                informacion += str(museo.nombre) + ": <a href=" + str(museo.url)+ ">Acceder al museo</a><br>"


        c =({'enlace_mipagina': enlace_mipagina,'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'lista_museos': informacion})
        template = get_template("museos/index.html")
        return HttpResponse(template.render(c))

    else:
        num = Museo.objects.all()
        if int(len(num)) == 0:
            theParser = make_parser()
            theHandler = myContentHandler()
            theParser.setContentHandler(theHandler)
            xmlFile = urllib.request.urlopen('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')
            theParser.parse(xmlFile)

            lista=""
            lista_usuarios = User.objects.all()
            for usuario in lista_usuarios:
                lista += str(usuario) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"

            c =({'enlace_mipagina': enlace_mipagina, 'registro' : logged, 'color' : color, 'tamaño' : tamaño,'formulario' : formulario, 'usuarios' : "<div id='box_users'><h4>Usuarios de la página:</h4>" +lista+"</div>"})
            template = get_template("museos/index.html")
            return HttpResponse(template.render(c))

        else:

            lista_users=""
            lista_usuarios = User.objects.all()
            for usuario in lista_usuarios:

                lista_usuarios_aux = Usuario.objects.all()
                encontrado = False
                for usuario_aux in lista_usuarios_aux:
                    if usuario_aux.usuario == usuario.username:
                        titulo_pagina = usuario_aux.titulo
                        encontrado = True
                if encontrado == False:
                        titulo_pagina = ""


                if str(titulo_pagina) == "":
                    lista_users += str(usuario) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"
                else:
                    lista_users += str(titulo_pagina) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"

            #MUESTRO LA LISTA DE MUSEOS Y DEPLEGABLE DE 5 EN 5
            lista= Museo.objects.all()
            for museo in lista:
                dic_comentarios[museo.id] = museo.comentarios

            lista_ordenada = sorted(dic_comentarios.items(), key=operator.itemgetter(1), reverse=True)
            lista_cinco = lista_ordenada[0:5]

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


            num_pagina = 5
            formulario_desplegable = """
                                        <form action=""" + str(num_pagina) + """ method="POST">
                                        <input class="button log-out" type="submit" value="VER MAS">
                                        </form>
                                        """



            info_museo_1 = "<div class='box_muse'><h3><a href=" + str(url[0]) + ">" + str(m[0]) + "</a></br>" + str(clase[0]) + " " + str(via[0]) + " " + str(tipo[0]) + " " + str(num[0]) + " " + str(localidad[0]) + " " + str(provincia[0]) + "</br>" + str(codigo[0]) + " " + str(barrio[0]) + "</br>" + str(distrito[0]) + "</br><a href=" + "/museo/" + str(lista_id[0]) + ">" + "Mas información" + "</a></h3></div>"
            info_museo_2 = "<div class='box_muse'><h3><a href=" + str(url[1]) + ">" + str(m[1]) + "</a></br>" + str(clase[1]) + " " + str(via[1]) + " " + str(tipo[1]) + " " + str(num[1]) + " " + str(localidad[1]) + " " + str(provincia[1]) + "</br>" + str(codigo[1]) + " " + str(barrio[1]) + "</br>" + str(distrito[1]) + "</br><a href=" + "/museo/" + str(lista_id[1]) + ">" + "Mas información" + "</a></h3></div>"
            info_museo_3 = "<div class='box_muse'><h3><a href=" + str(url[2]) + ">" + str(m[2]) + "</a></br>" + str(clase[2]) + " " + str(via[2]) + " " + str(tipo[2]) + " " + str(num[2]) + " " + str(localidad[2]) + " " + str(provincia[2]) + "</br>" + str(codigo[2]) + " " + str(barrio[2]) + "</br>" + str(distrito[2]) + "</br><a href=" + "/museo/" + str(lista_id[2]) + ">" + "Mas información" + "</a></h3></div>"
            info_museo_4 = "<div class='box_muse'><h3><a href=" + str(url[3]) + ">" + str(m[3]) + "</a></br>" + str(clase[3]) + " " + str(via[3]) + " " + str(tipo[3]) + " " + str(num[3]) + " " + str(localidad[3]) + " " + str(provincia[3]) + "</br>" + str(codigo[3]) + " " + str(barrio[3]) + "</br>" + str(distrito[3]) + "</br><a href=" + "/museo/" + str(lista_id[3]) + ">" + "Mas información" + "</a></h3></div>"
            info_museo_5 = "<div class='box_muse'><h3><a href=" + str(url[4]) + ">" + str(m[4]) + "</a></br>" + str(clase[4]) + " " + str(via[4]) + " " + str(tipo[4]) + " " + str(num[4]) + " " + str(localidad[4]) + " " + str(provincia[4]) + "</br>" + str(codigo[4]) + " " + str(barrio[4]) + "</br>" + str(distrito[4]) + "</br><a href=" + "/museo/" + str(lista_id[4]) + ">" + "Mas información" + "</a></h3></div>"

            c =({'enlace_mipagina': enlace_mipagina,'filtro_accesibilidad': formulario_filtro_accesibilidad, 'color' : color, 'tamaño' : tamaño, 'registro' : logged, 'museo1' : info_museo_1, 'museo2' : info_museo_2, 'museo3' : info_museo_3, 'museo4' : info_museo_4,'museo5' : info_museo_5, 'desplegable': formulario_desplegable,  'usuarios' : "<div id='box_users'><h4>Usuarios de la página:</h4>" + lista_users+"</div>"})
            template = get_template("museos/index_museos.html")
            return HttpResponse(template.render(c))


@csrf_exempt
def principal_anotada(request, num_pagina):

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
        logged = 'Logged in as: ' + request.user.username + '<br> <a class="button log-out" href= "/logout">Logout</a> <br>'
        lista_usuarios = Usuario.objects.all()
        encontrado = False
        for usuario in lista_usuarios:
            if usuario.usuario == request.user.username:
                titulo = usuario.titulo
                color = usuario.color
                tamaño = usuario.tamaño
                encontrado = True
        if encontrado == False:
                titulo = ""
                color = ""
                tamaño = ""
    else:
        enlace_mipagina = ""
        logged = 'Not logged in. <br>' + '<a class="button log-out" href= "/login">Login</a> <br>'
        titulo = ""
        color = ""
        tamaño = ""

    lista_aux = ""
    lista_usuarios = User.objects.all()
    for usuario in lista_usuarios:

        lista_usuarios_aux = Usuario.objects.all()
        encontrado = False
        for usuario_aux in lista_usuarios_aux:
            if usuario_aux.usuario == usuario.username:
                titulo_pagina = usuario_aux.titulo
                encontrado = True
        if encontrado == False:
                titulo_pagina = ""


        if str(titulo_pagina) == "":
            lista_aux += str(usuario) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"
        else:
            lista_aux += str(titulo_pagina) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"

    lista_users=""
    lista_usuarios = User.objects.all()
    for usuario in lista_usuarios:
        lista_users += str(usuario) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"

    lista=""
    lista_usuarios = User.objects.all()
    for usuario in lista_usuarios:
        lista += str(usuario) + ": <a href=" + str(usuario) + ">" + str(usuario) + "</a></br>"

    #MUESTRO LA LISTA DE MUSEOS Y DEPLEGABLE DE 5 EN 5
    lista= Museo.objects.all()
    for museo in lista:
        dic_comentarios[museo.id] = museo.comentarios

    lista_ordenada = sorted(dic_comentarios.items(), key=operator.itemgetter(1), reverse=True)
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
                                <input class="button log-out" type="submit" value="VER MAS">
                                </form>
                                """



    info_museo_1 = "<div class='box_muse'><h3><a href=" + str(url[0]) + ">" + str(m[0]) + "</a></br>" + str(clase[0]) + " " + str(via[0]) + " " + str(tipo[0]) + " " + str(num[0]) + " " + str(localidad[0]) + " " + str(provincia[0]) + "</br>" + str(codigo[0]) + " " + str(barrio[0]) + "</br>" + str(distrito[0]) + "</br><a href=" + "/museo/" + str(lista_id[0]) + ">" + "Mas información" + "</a></h3></div>"
    info_museo_2 = "<div class='box_muse'><h3><a href=" + str(url[1]) + ">" + str(m[1]) + "</a></br>" + str(clase[1]) + " " + str(via[1]) + " " + str(tipo[1]) + " " + str(num[1]) + " " + str(localidad[1]) + " " + str(provincia[1]) + "</br>" + str(codigo[1]) + " " + str(barrio[1]) + "</br>" + str(distrito[1]) + "</br><a href=" + "/museo/" + str(lista_id[1]) + ">" + "Mas información" + "</a></h3></div>"
    info_museo_3 = "<div class='box_muse'><h3><a href=" + str(url[2]) + ">" + str(m[2]) + "</a></br>" + str(clase[2]) + " " + str(via[2]) + " " + str(tipo[2]) + " " + str(num[2]) + " " + str(localidad[2]) + " " + str(provincia[2]) + "</br>" + str(codigo[2]) + " " + str(barrio[2]) + "</br>" + str(distrito[2]) + "</br><a href=" + "/museo/" + str(lista_id[2]) + ">" + "Mas información" + "</a></h3></div>"
    info_museo_4 = "<div class='box_muse'><h3><a href=" + str(url[3]) + ">" + str(m[3]) + "</a></br>" + str(clase[3]) + " " + str(via[3]) + " " + str(tipo[3]) + " " + str(num[3]) + " " + str(localidad[3]) + " " + str(provincia[3]) + "</br>" + str(codigo[3]) + " " + str(barrio[3]) + "</br>" + str(distrito[3]) + "</br><a href=" + "/museo/" + str(lista_id[3]) + ">" + "Mas información" + "</a></h3></div>"
    info_museo_5 = "<div class='box_muse'><h3><a href=" + str(url[4]) + ">" + str(m[4]) + "</a></br>" + str(clase[4]) + " " + str(via[4]) + " " + str(tipo[4]) + " " + str(num[4]) + " " + str(localidad[4]) + " " + str(provincia[4]) + "</br>" + str(codigo[4]) + " " + str(barrio[4]) + "</br>" + str(distrito[4]) + "</br><a href=" + "/museo/" + str(lista_id[4]) + ">" + "Mas información" + "</a></h3></div>"

    c =({'enlace_mipagina': enlace_mipagina, 'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'museo1' : info_museo_1, 'museo2' : info_museo_2, 'museo3' : info_museo_3, 'museo4' : info_museo_4,'museo5' : info_museo_5, 'desplegable': formulario_desplegable, 'usuarios' : "<div id='box_users'><h4>Usuarios de la página:</h4>" + lista_aux})
    template = get_template("museos/index_museos.html")
    return HttpResponse(template.render(c))


@csrf_exempt
def usuario(request, id_usuario):

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
        if id_usuario == request.user.username:
            formulario_color = """</br></br></br></br></br>
                                        <div>
                                        <form action="" method="POST">
                                        Cambiar color de fondo: <input type="text" name="color"><br>
                                        <input class="button log-out" type="submit" name="tipo" value="CAMBIAR COLOR"/>
                                        </form>
                                        </div></br></br></br></br></br></br>"""

            formulario_tamaño = """
                                        <div>
                                        <form action="" method="POST">
                                        Cambiar tamaño de letra: <input type="text" name="tamaño"><br>
                                        <input class="button log-out" type="submit" name="tipo" value="CAMBIAR TAMAÑO"/>
                                        </form>
                                        </div></br></br></br></br></br></br>
                                        """

            formulario_titulo = """
                                        <div>
                                        <form action="" method="POST">
                                        Cambiar título de la página: <input type="text" name="titulo"><br>
                                        <input class="button log-out" type="submit" name="tipo" value="CAMBIAR TÍTULO"/>
                                        </form>
                                        </div></br></br></br></br></br></br>
                                        """
        else:
            formulario_color = ""
            formulario_tamaño = ""
            formulario_titulo = ""
    else:
        formulario_color = ""
        formulario_tamaño = ""
        formulario_titulo = ""
        enlace_mipagina = ""

    lista_usuarios = Usuario.objects.all()
    encontrado = False
    for usuario in lista_usuarios:
        if usuario.usuario == request.user.username:
            color = usuario.color
            tamaño = usuario.tamaño
            encontrado = True
    if encontrado == False:
            color = ""
            tamaño = ""

    lista_usuarios = Usuario.objects.all()
    encontrado = False
    for usuario in lista_usuarios:
        if usuario.usuario == id_usuario:
            titulo = usuario.titulo
            encontrado = True
    if encontrado == False:
            titulo = ""


    num_pagina = 5
    formulario_desplegable = """
                            <form action=""" + str(request.user.username) + """/""" + str(num_pagina) + """ method="POST">
                            <input class="button log-out" type="submit" value="VER MÁS">
                            </form>
                            """




    if request.method == "POST":
        if str(request.POST['tipo']) == "CAMBIAR COLOR":
            lista_usuarios = Usuario.objects.all()
            if len(lista_usuarios)==0:
                nuevo_atributo = Usuario(color=request.POST.get("color",""),usuario=id_usuario)
                nuevo_atributo.save()
            else:
                encontrado = False
                for usuario in lista_usuarios:
                    if usuario.usuario == id_usuario:
                        usuario.color = request.POST.get("color","")
                        usuario.save()
                        encontrado = True

                if encontrado == False:
                    nuevo_atributo = Usuario(color=request.POST.get("color",""),usuario=id_usuario)
                    nuevo_atributo.save()

            c =({'enlace_mipagina': enlace_mipagina, 'color' : color, 'tamaño' : tamaño, 'contenido' : "Hemos añadido el color a la base de datos. Gracias."})
            template = get_template("museos/index.html")
            return HttpResponse(template.render(c))

        elif str(request.POST['tipo']) == "CAMBIAR TAMAÑO":
            lista_usuarios = Usuario.objects.all()
            if len(lista_usuarios)==0:
                nuevo_atributo = Usuario(color=request.POST.get("color",""),usuario=id_usuario)
                nuevo_atributo.save()
            else:
                encontrado = False
                for usuario in lista_usuarios:
                    if usuario.usuario == id_usuario:
                        usuario.tamaño = request.POST.get("tamaño","")
                        usuario.save()
                        encontrado=True

                if encontrado == False:
                    nuevo_atributo = Usuario(tamaño=request.POST.get("tamaño",""),usuario=id_usuario)
                    nuevo_atributo.save()

            c =({'enlace_mipagina': enlace_mipagina, 'color' : color, 'tamaño' : tamaño, 'contenido' : "Hemos añadido el tamaño a la base de datos. Gracias."})
            template = get_template("museos/index.html")
            return HttpResponse(template.render(c))

        else:

            lista_usuarios = Usuario.objects.all()
            if len(lista_usuarios)==0:
                nuevo_atributo = Usuario(titulo=request.POST.get("titulo",""),usuario=id_usuario)
                nuevo_atributo.save()
            else:
                encontrado = False
                for usuario in lista_usuarios:
                    if usuario.usuario == id_usuario:
                        usuario.titulo = request.POST.get("titulo","")
                        usuario.save()
                        encontrado=True

                if encontrado == False:
                    nuevo_atributo = Usuario(titulo=request.POST.get("titulo",""),usuario=id_usuario)
                    nuevo_atributo.save()

            c =({'enlace_mipagina': enlace_mipagina, 'color' : color, 'tamaño' : tamaño, 'contenido' : "Hemos añadido el título a la base de datos. Gracias."})
            template = get_template("museos/index.html")
            return HttpResponse(template.render(c))
    else:

        info_museo = ""
        lista_museos_usuario = Museo_Usuario.objects.all()

        lista_cinco_museos = lista_museos_usuario[0:5]
        for museo in lista_cinco_museos:
            if museo.usuario == id_usuario:
                identificador = museo.id_museo
                nombre = Museo.objects.get(id=identificador)
                nom_str="<h2>"+str(nombre)+"</h2>"
                via=nombre.via
                clase=nombre.clase
                tipo=nombre.tipo
                num=nombre.num
                localidad=nombre.localidad
                provincia=nombre.provincia
                codigo=nombre.codigo
                barrio=nombre.barrio
                distrito=nombre.distrito
                url=nombre.url
                info_museo+="<div>"+str(nom_str)+"<h3>"+str(clase)+" "+str(via)+" "+str(tipo)+" "+str(num)+"</h3><p>"+str(localidad)+"</p><p>"+str(provincia)+"</p><p>"+str(codigo)+"</p><p>"+str(barrio)+"</p><p>"+str(distrito) + "<p>" + "El museo fue añadido: " + str(museo.fecha) + "</p><p><a href="+str(url)+">Más info</a></p></div>"
        c =({'enlace_mipagina': enlace_mipagina, 'titulo': titulo,'color' : color, 'tamaño' : tamaño, 'contenido' : info_museo, 'desplegable' : formulario_desplegable, 'formulario_titulo':formulario_titulo, 'formulario_color': formulario_color, 'formulario_tamaño': formulario_tamaño})
        template = get_template("museos/index.html")
        return HttpResponse(template.render(c))


@csrf_exempt
def usuario_anotada(request, usuario, num_pagina):

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
    else:
        enlace_mipagina = ""

    lista_usuarios = Usuario.objects.all()
    encontrado = False
    for usuario in lista_usuarios:
        if usuario.usuario == request.user.username:
            color = usuario.color
            tamaño = usuario.tamaño
            encontrado = True
    if encontrado == False:
            color = ""
            tamaño = ""

    lista_usuarios = Usuario.objects.all()
    encontrado = False
    for usuario in lista_usuarios:
        if usuario.usuario == id_usuario:
            titulo = usuario.titulo
            encontrado = True
    if encontrado == False:
            titulo = ""


    info_museo = ""
    lista_museos_usuario = Museo_Usuario.objects.all()

    lista_cinco_museos = lista_museos_usuario[int(num_pagina):int(num_pagina)+5]
    for museo in lista_cinco_museos:
        if museo.usuario == usuario:

            identificador = museo.id_museo
            nombre = Museo.objects.get(id=identificador)
            nom_str="Nombre: <h2>"+str(nombre)+"</h2>"
            via=nombre.via
            clase=nombre.clase
            tipo=nombre.tipo
            num=nombre.num
            localidad=nombre.localidad
            provincia=nombre.provincia
            codigo=nombre.codigo
            barrio=nombre.barrio
            distrito=nombre.distrito
            url=nombre.url
            info_museo+="<div>"+str(nom_str)+"<h3>"+str(clase)+" "+str(via)+" "+str(tipo)+" "+str(num)+"</h3><p>"+str(localidad)+"</p><p>"+str(provincia)+"</p><p>"+str(codigo)+"</p><p>"+str(barrio)+"</p><p>"+str(distrito)+"<p>" + "El museo fue añadido: " + str(museo.fecha) + "</p></p><p><a href="+str(url)+">Más info</a></p></div>"

    num_pagina = int(num_pagina) + 5
    formulario_desplegable = """
                            <form action=""" + str(num_pagina) + """ method="POST">
                            <input class="button log-out" type="submit" value="VER MAS">
                            </form>
                            """

    if len(lista_cinco_museos) == 0:
        info = "NO HAY MÁS MUSEOS QUE MOSTRAR"

    c =({'enlace_mipagina': enlace_mipagina, 'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'contenido' : info + info_museo, 'desplegable' : formulario_desplegable})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))


@csrf_exempt
def usuario_xml(request,nombre_usuario):

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
        logged = 'Logged in as: ' + request.user.username + '<br> <a class="button log-out" href= "/logout">Logout</a> <br>'
        lista_usuarios = Usuario.objects.all()
        encontrado = False
        for usuario in lista_usuarios:
            if usuario.usuario == request.user.username:
                titulo = usuario.titulo
                color = usuario.color
                tamaño = usuario.tamaño
                encontrado = True
        if encontrado == False:
                titulo = ""
                color = ""
                tamaño = ""
    else:
        enlace_mipagina = ""
        logged = 'Not logged in. <br>' + '<a class="button log-out" href= "/login">Login</a> <br>'
        titulo = ""
        color = ""
        tamaño = ""

    xml = "<?xml version='1.0' encoding='UTF-8' ?>\n<contenidos>"
    print("USUARIO: " + str(nombre_usuario))

    lista_museos_usuario = Museo_Usuario.objects.all()
    for museo in lista_museos_usuario:
        if museo.usuario == nombre_usuario:
            identificador = museo.id_museo
            nombre = Museo.objects.get(id=identificador)
            nom_str="<h2>"+str(nombre)+"</h2>"
            entidad=nombre.entidad
            horario=nombre.horario
            descripcion=nombre.descripcion
            transporte=nombre.transporte
            accesibilidad=nombre.accesibilidad
            via=nombre.via
            clase=nombre.clase
            tipo=nombre.tipo
            num=nombre.num
            localidad=nombre.localidad
            provincia=nombre.provincia
            codigo=nombre.codigo
            barrio=nombre.barrio
            distrito=nombre.distrito
            url=nombre.url
            telefono = nombre.telefono
            fax =nombre.fax
            email = nombre.email

            xml += "<contenido>\n<tipo>EntidadesYOrganismos</tipo>\n<atributo nombre='ID-ENTIDAD'>"+str(entidad)+"</atributo>\n<atributo nombre='NOMBRE'>"+str(nombre)+"</atributo>\n<atributo nombre='DESCRIPCION-ENTIDAD'>"+str(descripcion)+"</atributo><atributo nombre='HORARIO'>"+str(horario)+"</atributo><atributo nombre='TRANSPORTE'>"+str(transporte)+"</atributo><atributo nombre='ACCESIBILIDAD'>"+str(accesibilidad)+"</atributo><atributo nombre='NOMBRE-VIA'>"+str(via)+"</atributo><atributo nombre='CLASE-VIAL'>"+str(clase)+"</atributo>\n<atributo nombre='TIPO-NUM'>"+str(tipo)+"</atributo>\n<atributo nombre='NUM'>"+str(num)+"</atributo>\n<atributo nombre='LOCALIDAD'>"+str(localidad)+"</atributo><atributo nombre='PROVINCIA'>"+str(provincia)+"</atributo><atributo nombre='CODIGO-POSTAL'>"+str(codigo)+"</atributo><atributo nombre='BARRIO'>"+str(barrio)+"</atributo><atributo nombre='DISTRITO'>"+str(distrito)+"</atributo><atributo nombre='TELEFONO'>"+str(telefono)+"</atributo>\n<atributo nombre='FAX'>"+str(fax)+"</atributo>\n<atributo nombre='EMAIL'>"+str("hola")+"</atributo>\n</contenido>\n"

    xml += "</contenidos>"

    return HttpResponse(str(xml), content_type="text/xml")


@csrf_exempt
def museos(request):

    formulario_filtro = """
                        <form action="" method="POST">
                        Buscar por distrito: <input type="text" name="distrito"><br>
                        <input class="button log-out" type="submit" value="VER">
                        </form>
                        """


    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
        logged = 'Logged in as: ' + request.user.username + '<br> <a class="button log-out" href= "/logout">Logout</a> <br>'
        lista_usuarios = Usuario.objects.all()
        encontrado = False
        for usuario in lista_usuarios:
            if usuario.usuario == request.user.username:
                titulo = usuario.titulo
                color = usuario.color
                tamaño = usuario.tamaño
                encontrado = True
        if encontrado == False:
                titulo = ""
                color = ""
                tamaño = ""
    else:
        enlace_mipagina = ""
        logged = 'Not logged in. <br>' + '<a class="button log-out" href= "/login">Login</a> <br>'
        titulo = ""
        color = ""
        tamaño = ""

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

        c =({'enlace_mipagina': enlace_mipagina, 'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'lista_museos': informacion})
        template = get_template("museos/index.html")
        return HttpResponse(template.render(c))

    else:

        informacion = ""
        lista = Museo.objects.all()
        for museo in lista:
            informacion += str(museo.nombre) + ": <a href=" + str(museo.url)+ ">Acceder al museo</a><br>"

        c =({'enlace_mipagina': enlace_mipagina,'formulario_filtro': formulario_filtro, 'color' : color, 'tamaño' : tamaño ,'registro' : logged, 'lista_museos': informacion})
        template = get_template("museos/index.html")
        return HttpResponse(template.render(c))


@csrf_exempt
def museo_id(request, identificador):

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href=/"+str(request.user.username)+">Mi Página</a></li>"
        logged = 'Logged in as: ' + request.user.username + '<br> <a class="button log-out" href= "/logout">Logout</a> <br>'
        lista_usuarios = Usuario.objects.all()
        encontrado = False
        for usuario in lista_usuarios:
            if usuario.usuario == request.user.username:
                titulo = usuario.titulo
                color = usuario.color
                tamaño = usuario.tamaño
                encontrado = True
        if encontrado == False:
                titulo = ""
                color = ""
                tamaño = ""
    else:
        enlace_mipagina = ""
        logged = 'Not logged in. <br>' + '<a class="button log-out" href= "/login">Login</a> <br>'
        titulo = ""
        color = ""
        tamaño = ""

    formulario_add = """<div>
                    <form action="" method="POST">
                    <input class="button log-out" type="submit" name="flag" value="AÑADIR A MI LISTA DE MUSEOS" />
                    </form>
                    </div>"""

    formulario_comentario = """
                        <div>
                        <form action="" method="POST">
                        <textarea name="comentario" rows="10" placeholder="Escribe aquí tus comentarios" cols="40"></textarea>
                        <input class="button log-out" type="submit" name="flag" value="AÑADIR COMENTARIO"/>
                        </form>
                        </div>
                        """



    if request.user.is_authenticated():
        if request.method == "POST":

            if str(request.POST['flag']) == "AÑADIR A MI LISTA DE MUSEOS":

                nuevo_museo = Museo_Usuario(usuario=request.user.username, id_museo=identificador, fecha=datetime.datetime.now())
                nuevo_museo.save()

                c =({'enlace_mipagina': enlace_mipagina,'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'contenido' : "Museo añadido a su lista de museos"})
                template = get_template("museos/index.html")
                return HttpResponse(template.render(c))

            else: #añadir a la base de datos de comentarios
                nuevo_comentario = Comentario(comentario=request.POST.get("comentario",""), id_museo=identificador)
                nuevo_comentario.save()

                museo = Museo.objects.get(id=identificador)
                num_comentarios = museo.comentarios
                museo.comentarios=int(num_comentarios)+1
                museo.save()
                c =({'enlace_mipagina': enlace_mipagina,'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'contenido' : "Hemos añadido su comentario. Muchas gracias."})
                template = get_template("museos/index.html")
                return HttpResponse(template.render(c))

        else:
            nombre = Museo.objects.get(id=identificador)
            lista = Museo.objects.all()
            for museo in lista:
                if museo.nombre == str(nombre):
                    if museo.accesibilidad == 0:
                        accesibilidad = "El museo es accesible. "
                    else:
                        accesibilidad = "El museo no es accesible. "
                    informacion = museo.nombre + "</br></br>" + museo.descripcion + "</br></br>" + museo.transporte + "</br></br>" + accesibilidad + "</br></br>" +  "<a href=" + str(museo.url) + ">Ver museo</a>" + "</br></br>Dirección: </br>" + museo.clase + " " + museo.via + "</br>" + museo.localidad + "</br>" + museo.provincia + "</br>" + museo.codigo + "</br></br>" + "Barrio: " + museo.barrio + "</br>" + "Distrito: " + museo.distrito + "</br></br>Datos de contacto: </br>" + "Teléfono: " + museo.telefono + "</br>" + "Fax: " + museo.fax + "</br>Email: " + museo.email

            string = "</br></br></br></br><div>"
            lista_comentarios = Comentario.objects.all()
            for comentario in lista_comentarios:
                if comentario.id_museo == identificador:
                    string += "<p>" + comentario.comentario + "</p>"

            string += "</div>"

            c =({'enlace_mipagina': enlace_mipagina,'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'contenido' : informacion, 'formulario_add': formulario_add, 'formulario_comentario' : formulario_comentario, 'comentarios': string})
            template = get_template("museos/index.html")
            return HttpResponse(template.render(c))
    else:

        nombre = Museo.objects.get(id=identificador)
        lista = Museo.objects.all()
        for museo in lista:
            if museo.nombre == str(nombre):
                if museo.accesibilidad == 0:
                    accesibilidad = "El museo es accesible. "
                else:
                    accesibilidad = "El museo no es accesible. "
                informacion = museo.nombre + "</br></br>" + museo.descripcion + "</br></br>" + museo.transporte + "</br></br>" + accesibilidad + "</br></br>" +  "<a href=" + str(museo.url) + ">Ver museo</a>" + "</br></br>Dirección: </br>" + museo.clase + " " + museo.via + "</br>" + museo.localidad + "</br>" + museo.provincia + "</br>" + museo.codigo + "</br></br>" + "Barrio: " + museo.barrio + "</br>" + "Distrito: " + museo.distrito + "</br></br>Datos de contacto: </br>" + "Teléfono: " + museo.telefono + "</br>" + "Fax: " + museo.fax + "</br>Email: " + museo.email

        string = "</br></br></br></br><div>"
        lista_comentarios = Comentario.objects.all()
        for comentario in lista_comentarios:
            if comentario.id_museo == identificador:
                string += "<p>" + comentario.comentario + "</p>"
        string += "</div>"

        c =({'enlace_mipagina': enlace_mipagina,'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'contenido' : informacion, 'comentarios': string})
        template = get_template("museos/index.html")
        return HttpResponse(template.render(c))


@csrf_exempt
def about(request):

    if request.user.is_authenticated():
        enlace_mipagina = "<li><a href="+str(request.user.username)+">Mi Página</a></li>"
        logged = 'Logged in as: ' + request.user.username + '<br> <a class="button log-out" href= "/logout">Logout</a> <br>'
        lista_usuarios = Usuario.objects.all()
        encontrado = False
        for usuario in lista_usuarios:
            if usuario.usuario == request.user.username:
                titulo = usuario.titulo
                color = usuario.color
                tamaño = usuario.tamaño
                encontrado = True
        if encontrado == False:
                titulo = ""
                color = ""
                tamaño = ""
    else:
        enlace_mipagina = ""
        logged = 'Not logged in. <br>' + '<a class="button log-out" href= "/login">Login</a> <br>'
        titulo = ""
        color = ""
        tamaño = ""

    about = "<!doctype html><html><head><h1>Información sobre la aplicación</h1></head><h3>Breve descripción del sitio y su funcionalidad</h3><br><body>Esta página trata de crear un portal donde la gente puede obtener información sobre todos los museos de la Comunidad de Madrid. Además, puede escribir comentarios si es un usuario registrado. Los usuarios que se registren cuentan con una página propia donde pueden elegir un título para su página, el color de fondo para el sitio y el tamaño de letra. Además, puede ir añadiendo museos a su página personal.</br></br>La página principal, consta de cinco museos y un botón a través del cual pueden ver los cinco siguientes museos de la lista, también de una lista con los usuarios registrados y además un filtro de accesibilidad, que muestra solo los museos accesibles. </br></br>En la pestaña Lista de Museos, pueden ver una lista con todos los museos y filtrarlos por distrito. Pueden acceder a información más detallada sobre un museo pinchando en el enlace del museo en cuestión. </br></br>Nuestra página web también permite mostrar el XML con la lista de musesos seleccionados de cada uno de nuestros usuarios registrados.</br></br><p>Esta aplicación web, es un proyecto para la asignatura de Servicios y Aplicaciones en Reder de Ordenadores.</p></br><p>Autora: Natalia Alonso Arteaga.</p></br></body></html>"

    c =({'enlace_mipagina': enlace_mipagina,'registro' : logged, 'color' : color, 'tamaño' : tamaño, 'contenido' : str(about), 'color' : color, 'tamaño' : tamaño})
    template = get_template("museos/index.html")
    return HttpResponse(template.render(c))
