from flask import Flask, render_template
from flask import request
import json
import fichero          #Realizamos las operaciones sobre el fichero de lectura, escritura

app = Flask(__name__)

@app.route('/contenido', methods=['GET'])
def contenido():    
    data = fichero.leer_fichero()     
    return render_template('contenido.html',data=data, mensaje_control = '')

@app.route('/registrar', methods=['POST'])
def registrar():
    if(fichero.crear_fichero(request.form)):
        mensaje_control = 'Usuario creado correctamente'        
    else:
        mensaje_control = 'Ha ocurrido un error, no se ha podido crear el usuario'
    return render_template('anadir.html',mensaje_control = mensaje_control)  

@app.route('/ver/<id>', methods = ['GET']) 
def ver(id): 
    datos = json.loads(fichero.buscar_registro(id))
    return render_template('editar.html',datos = datos)   

@app.route('/', methods=['GET'])
def login():
    return render_template('index.html')

@app.route('/anadir', methods=['GET'])
def index():
    return render_template('anadir.html')   
    

@app.route('/eliminar', methods =['POST'])
def eliminar():
    mensaje_control = fichero.borrar_registro(request.form['id'])
    data = fichero.leer_fichero()
    return render_template('contenido.html',data=data, mensaje_control = mensaje_control)


@app.route('/actualizar', methods =['POST'])
def actualizar():
    fichero.borrar_registro(request.form['id']) #Borramos el registro
    if (fichero.crear_fichero(request.form)):#Creamos el nuevo actualizado
        mensaje_control = "Registro actualizado correctamente"
    data = fichero.leer_fichero()
    return render_template('contenido.html',data=data, mensaje_control = mensaje_control)  

if __name__ == "__main__":    
    app.run(debug=True)