from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from .models import Museo
import urllib.request
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

class myContentHandler(ContentHandler):

    def __init__ (self):

        self.inItem = False
        self.inContent = False
        self.theContent = ""

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):

        global html

        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                line = "Titulo: " + self.theContent + "."
                html += "<li>" + '\n' + line + "</li>" + '\n'
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                link = self.theContent
                html += "<li><a href=" + link + ">Link</a></li>"

                self.inContent = False
                self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


formulario = """
<form action="" method="POST">
    Nombre: <input type="text" name="nombre"><br>
    Direccion: <input type="text" name="direccion"><br>
    Distrito: <input type="text" name="distrito"><br>
    Precio: <input type="text" name="precio"><br><br>
    <input type="submit" value="Enviar">
</form>
"""

def museo(request):


    html = "<br>LINKS DE BARRAPUNTO<br><br>"
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)

    xmlFile = urllib.request.urlopen('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')




    if request.user.is_authenticated():
        logged = 'Logged in as: ' + request.user.username + '<br> <a href= "/logout">Logout</a> <br>'
    else:
        logged = 'Not logged in. <br>'

    museos = Museo.objects.all()

    salida = ' '

    for museo in museos:
        salida += '<li><a href= "museo/' + str(museo.id) + '">' + museo.nombre + '</a></li></br>'

    salida += formulario
    salida += logged
    template = get_template("museo/index.html")
    c =({'titulo' : "MUSEO", 'contenido' : salida})
    return HttpResponse(template.render(c))

@csrf_exempt

def viaje(request, number):
    if request.method == "POST":
        viaje = Viaje(destino=request.POST['destino'], locomocion=request.POST['locomocion'], alojamiento=request.POST['alojamiento'], precio=request.POST['precio'])
        viaje.save()
        number = viaje.id
    try:
        viaje = Viaje.objects.get(id=int(number))
    except Viaje.DoesNotExist:
        return HttpResponse("no existe" + formulario)
    respuesta = "Viaje: " + viaje.destino + "<br>"
    respuesta += "Locomocion: " + viaje.locomocion + "<br>"
    respuesta += "Precio: " + str(viaje.precio) + " euros" + "<br><br>"
    respuesta += formulario

    template = get_template("oneworld/index.html")
    c =({'title': "VIAJES", 'contenido': respuesta})
    return HttpResponse(template.render(c))
