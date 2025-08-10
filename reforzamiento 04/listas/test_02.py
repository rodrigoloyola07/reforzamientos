"""Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista."""

departamentos_lista = ["Lima", "La Libertad", "Puno", "Madre de Dios", "Loreto", "Ucayali"]

departamento_1 = input("Ingresa una departamento: ")
departamento_2 = input("Ingresa una departamento: ")

departamentos_lista.append(departamento_1)
departamentos_lista.pop(0)
departamentos_lista.insert(0, departamento_2)
print(departamentos_lista)
