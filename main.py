from tareas import *



print("===================================")
print(" BIENVENIDO AL GESTOR DE TAREAS ")
print("===================================")

while True:
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese la tarea: ")
        agregar_tarea(nombre)
        print("Tarea guardada correctamente")

    elif opcion == "2":
        tareas = listar_tareas()

        if not tareas:
            print("No hay tareas registradas")

        for i, tarea in enumerate(tareas):
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i}. {tarea['nombre']} [{estado}]")

    elif opcion == "3":
        indice = int(input("Ingrese índice de la tarea: "))
        completar_tarea(indice)
        print("Tarea completada")

    elif opcion == "4":
        indice = int(input("Ingrese índice de la tarea: "))
        eliminar_tarea(indice)
        print("Tarea eliminada")

    elif opcion == "5":
        texto = input("Ingrese texto a buscar: ")

        resultados = buscar_tarea(texto)

        if resultados:
            for tarea in resultados:
                print(tarea)
        else:
            print("No se encontraron tareas")

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
