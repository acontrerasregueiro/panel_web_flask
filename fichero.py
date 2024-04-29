import json
import os
import pandas as pandas
import uuid             #Para crear un id único para cada usuario ingresado

def crear_fichero(formulario):
    formulario = dict(formulario)
    #Aplicamos formato a todos los campos salvo email y contraseña
    for clave in formulario:
        if clave == 'email' or clave == 'contrasena':         
            pass
        else:
            formulario[clave] = formulario[clave].title()
   
    #comprobamos si existe el fichero
    formulario['id'] = uuid.uuid4().hex
    if os.path.exists("archivo.txt"):
        #si no existe lo creamos        
        formulario = json.dumps(formulario)
        fichero = open("archivo.txt", "a")
        fichero.write(formulario + '\n')
        fichero.close()
        return True
    else:
        #si existe añadimos contenido al final
        with open('archivo.txt', 'w') as fichero:
            formulario = json.dumps(formulario)
            fichero.write(formulario + '\n')
            return True

    
def leer_fichero():
    if os.path.exists("archivo.txt"):
        f = open('archivo.txt','r+')
        s = f.read()
        s=[ json.loads(s) for s in s.splitlines()]
        df=pandas.DataFrame(s)
        f.close()   
        return df
    else:
        df = pandas.DataFrame()
        return df 
    
def buscar_registro(id):
    #Buscamos el la linea que contiene el id y devolvemos su indice
    fichero = open('archivo.txt','r+')
    datos = fichero.readlines()
    indice = 0
    registro = {}
    for linea in datos:
        if (id) in linea:
            print("Encontrado el id en el indice nº ",indice )
            print('registro ' ,linea)
            registro = linea
            break
    fichero.close() 
    return registro 
 
def borrar_registro(id):
    mensaje_control = 'Registro no encontrado'
    
    with open("archivo.txt", "r") as fichero:
       lineas = fichero.readlines()
    fichero.close()
    with open("archivo.txt", "w") as fichero:
        for linea in lineas:
            if (id) not in linea:
                fichero.write(linea)
            else:
                mensaje_control = "Registro encontrado y borrado correctamente" 
    fichero.close()
    return(mensaje_control)

def leer_registro(indice):
    #Accedemos directamente a la línea indice y leemos sus datos
    indice = int(indice)
    with open('archivo.txt','r') as fichero:
        datos = fichero.readlines()
    fichero.close()
    return (datos[indice])
    
    