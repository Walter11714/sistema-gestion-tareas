import json
import os

ARCHIVO = "data/tareas.json"

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as archivo:
        return json.load(archivo)

def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def agregar_tarea(nombre):
    tareas = cargar_tareas()

    tarea = {
        "nombre": nombre,
        "completada": False
    }

    tareas.append(tarea)
    guardar_tareas(tareas)

def listar_tareas():
    return cargar_tareas()

def completar_tarea(indice):
    tareas = cargar_tareas()

    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)

def eliminar_tarea(indice):
    tareas = cargar_tareas()

    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        guardar_tareas(tareas)

def buscar_tarea(texto):
    tareas = cargar_tareas()

    resultados = []

    for tarea in tareas:
        if texto.lower() in tarea["nombre"].lower():
            resultados.append(tarea)

    return resultados