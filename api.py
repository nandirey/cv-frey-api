#!flask/bin/python
# -*- coding: UTF-8 -*-

from logging import info
from  flask import Flask, request, abort
from flask.json import jsonify


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR']= True

@app.route('/')

def index():
    info = {
        "mensaje" : "Bienvenido a la API del curriculum vitae de Frey.",
        "acciones" : [
            "GET /curriculum",
            "POST / mensajes"
        ]
    }
    return jsonify(info)
@app.route('/curriculum',methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/aguilas-calvas.jpg"
    cv = {
        "nombre" : "Fernando",
        "apellido" : "Rey",
        "residencia" : "Uruguay",
        "experiencia" : [{
            "posicion" : "< describe tu posicion >",
            "empresa" : "< nombre de tu empresa >",
            "desde" : "< cuando empezaste a trabajar >",
            "hasta" : "< si ya no trabaja mas, cuando >",
            "descripcion": "< detalles >"
        }],
        "educacion" : {
            "nivel" : "< nivel de tus estudios >",
            "titulo" : "< nombre de tu carrera >",
            "institucion" : "< donde estudiaste >",
            "facultad" : "< mas detalles >"
        },
        "intereses" : ["python", "apis", "enseñar"],
        "redes" : {
            "github" : "https://github.com/nahueltori",
            "twitter" : "https://twitter.com/nahueltori",
            "linkedin" : "https://www.linkedin.com/in/nahueltori"
        },
        "foto" : url_imagen
    }
    return jsonify(cv)

@app.route('/mensajes',methods=['POST'])
def contacto():
    mensaje = request.get_data()

    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")
    
    print("Mensaje de contacto: " + str(mensaje))
    return "Gracias por su mensaje."  

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()