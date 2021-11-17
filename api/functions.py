from db import engine
from querys import *
from flask_sqlalchemy import SQLAlchemy


query = Query()
def listar_mascotas():
    try:
        mascotas = engine.execute(query.mascotas()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_mascotas = []
    for i in mascotas:
        lista_mascotas.append(i[1])
    return lista_mascotas 
def listar_mascotas_no_adoptadas():
    try:
        mascotas = engine.execute(query.no_adoptadas()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_mascotas_no_adoptadas = []
    for i in mascotas:
        lista_mascotas_no_adoptadas.append(i[1])
    return lista_mascotas_no_adoptadas 

def cantidad_tipo_mascotas():
    try:
        mascotas = engine.execute(query.cantidad_mascotas()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_mascotas_group = []
    for i in mascotas:
        dic={"Nombre":i[1],"cantidad":i[0]}
        lista_mascotas_group.append(dic)
    return lista_mascotas_group 
def propietarios_mascotas():
    try:
        mascotas = engine.execute(query.propietarios_mascotas()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_propietario_mascota = []
    for i in mascotas:
        dic={"Nombre":i[1],"cantidad_mascotas":i[0]}
        lista_propietario_mascota.append(dic)
    return lista_propietario_mascota
def can_mascotas_propietario():
    try:
        mascotas = engine.execute(query.propietarios_mascotas()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_can_pro_mas = []
    for i in mascotas:
        dic={"Nombre":i[1],"cantidad_mascotas":i[0]}
        lista_can_pro_mas.append(dic)
    return lista_propietario_mascota
def cant_mascotas_pro():
    try:
        mascotas = engine.execute(query.cant_mas_pro()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_cantidad_pr_mas = []
    for i in mascotas:
        dic={"Nombre":i[0],"tipo_mascota":i[1],"cantidad":i[2]}
        lista_cantidad_pr_mas.append(dic)
    return lista_cantidad_pr_mas 
def propietario_no_mascota():
    try:
        mascotas = engine.execute(query.propietario_no_mascota()) 
    except:
        return {"Respuesta":"Fallo consultando mascotas "}
    lista_propietario_no_mascota = []
    for i in mascotas:
        lista_propietario_no_mascota.append(i[0])
    return lista_propietario_no_mascota        