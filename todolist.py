# Mensaje de Bienvenida
print(f'¡Bienvenid@ a tu To-Do List creada con Python! ')
nombre = str(input("\n¿Cuál es tu nombre?\n"))

# Pregunta de consulta para ingresar a las opciones del To-Do List
pregunta = int(input("\n¿Deseas consultar tu To-Do List? \nElige 1 para sí o 2 para no\n"))

if pregunta == 1:
    # Crear una lista para almacenar las tareas
    tareas = []

    # Función para agregar una tarea
    def add_task(task):
        tareas.append(task)
        print("\nTarea agregada.")

    # Función para mostrar todas las tareas
    def show_tasks():
        if tareas:
            print("\nTareas:")
            for index, task in enumerate(tareas, start=1):
                print(f"{index}. {task}")
        else:
            print("\nNo hay tareas pendientes.")

    # Función para eliminar una tarea
    def remove_task(index):
        if 1 <= index <= len(tareas):
            del tareas[index - 1]
            print("\nTarea eliminada.")
        else:
            print("\nÍndice no válido.")

    # Loop para interactuar con el usuario
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            task = input("\nIngresa la tarea: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            index = int(input("\nIngresa el número de la tarea a eliminar: "))
            remove_task(index)
        elif choice == '4':
            print(f'\nGracias {nombre} por visitar tu To-Do List')
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


else:
    print("Gracias por visitar tu To-Do List")