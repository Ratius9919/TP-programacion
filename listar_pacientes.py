import os

def clear():
    os.system("cls")
    print()

def leer_pacientes(pos1, pos2):
    clear()
    f = open("Pacientes.txt", "r")
    listalistas = []

    for linea in (f):
        lista = linea[:-1].split(";")
        lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
        listalistas.append(lista)
        listalistas.sort()

    f.close()
    return listalistas

def mayores(edad):
    f = open("Pacientes.txt", "r")
    listalistas = []
    for linea in (f):
        lista = linea[:-1].split(";")
        lista[0], lista[2] = lista[2], lista[0]
        if int(lista[0]) > edad:
            listalistas.append(lista)
            listalistas.sort()
    
    f.close()

    return listalistas

def main():
    clear()  
    opcion = int(input("[?] Como desea obtener el listado de pacientes?\n\n[0] Nombre\n[1] Edad\n[2] Mayores a determinada edad\n\n[?] Opcion: "))

    if opcion == 0:

        clear()
        print("[+] Lista de pacientes registrados:\n")
        for i in leer_pacientes(0,1):
            print(f"Paciente: {i[0]} -- Edad: {i[2]} -- DNI: {i[1]}")
        print()

    if opcion == 1:

        clear()
        print("[+] Lista de pacientes registrados:\n")
        for i in leer_pacientes(0, 2):
            print(f"Paciente: {i[1]} -- Edad: {i[0]} -- DNI: {i[2]}")
        print()
    
    if opcion == 2:

        edad = int(input("[?] Ingrese la edad: "))

        clear()
        print("[+] Lista de pacientes registrados:\n")
        for i in mayores(edad):
            print(f"Paciente: {i[1]} -- Edad: {i[0]} -- DNI: {i[2]}")
        print()

    print()
    input("[+] Presione enter para continuar...")


if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")