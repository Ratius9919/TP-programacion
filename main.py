import os

from alta_pacientes import main as altapacientes
from listar_pacientes import main as listarpacientes
from listar_turnos import main as listarturnos
from baja_pacientes import main as bajapacientes
from alta_turnos import main as altaturnos
from modificar_pacientes import main as modificarpacientes
from buscar_turnos_dni import main as buscarturnos

# Funciones

def clear():
    os.system("cls")
    print()

def registrar(user, password):
    try: 
        with open("UsersDB.txt", "r") as usuarios:
            for i in usuarios:
                claves = i[:-1].split(";")
                if claves[0] == user:
                    print(f"[!] El nombre {user} ya fue elegido. Elija otro.\n")
                    input("[+] Volver al menu principal.")
                    break

            else: 
                    usuarios.write(f"{user};{password}\n")
                    return True
            usuarios.close()

    except:
        usuarios = open("UsersDB.txt", "a")
        usuarios.write(f"{user};{password}\n")
        usuarios.close()


def iniciar_sesion(user, password, usersdb):
    for registro in usersdb:
        claves = registro[:-1].split(";")
        if user == claves[0]:
            if claves[1] == password:
                return True

# Programa Principal

clear()
opcion = int(input("+++ [Sistema Medico] +++\n\n[1] Registro \n[2] Login \n\n[?] Opcion: "))

print()
while opcion not in [1, 2]:
    clear()
    opcion = int(input("+++ [Sistema Medico] +++\n\n[1] Registro \n[2] Login \n\n[?] Opcion: "))

while opcion in [1, 2]:
    if opcion == 1:
        clear()    
        user = input("[?] Nombre de usuario: ")
        password = input("[?] Contrasena: ")

        registro = registrar(user, password)
        if registro:
            print("\n[+] Registrado correctamente!\n")
            input("[+] Continuar..")
        clear()
        opcion = int(input("+++ [Sistema Medico] +++\n\n[1] Registro \n[2] Login \n\n[?] Opcion: "))

    if opcion == 2:
        clear()    
        user = input("[?] Nombre de usuario: ")
        password = input("[?] Contrasena: ")

        with open("UsersDB.txt", "r") as usersdb:
            inicio = iniciar_sesion(user, password, usersdb)
            if inicio:
                clear()
                usersdb.close()
                menuOption = int(input(F"[+] Bienvenido/a {user.upper()}, por favor, selecciona de las opciones a continuación para seguir: \n\n[1] - Alta Paciente \n[2] - Alta Turno \n[3] - Modificar Paciente \n[4] - Baja Paciente \n[5] - Lista por dia/mes \n[6] - Lista Pacientes \n[7] - Búsqueda de turnos por DNI \n[8] - Cargar datos de Prueba \n[0] - Cerrar consola\n\n[?] Opcion: "))
                while menuOption != 0:
                    if menuOption == 1:
                        altapacientes()

                    if menuOption == 2:
                        altaturnos()

                    if menuOption == 3:
                        modificarpacientes()

                    if menuOption == 4:
                        bajapacientes()

                    if menuOption == 5:
                        listarturnos()

                    if menuOption == 6:
                        listarpacientes()

                    if menuOption == 7:
                        buscarturnos()

                    if menuOption == 8:
                        print("Alta turno")

                    if menuOption < 1 or menuOption > 8:
                        menuOption = int(input("[!] Ha ingresado un valor incorrecto, ingrese una opción válida: "))
                    clear()
                    menuOption = int(input(F"[+] Bienvenido/a {user.upper()}, por favor, selecciona de las opciones a continuación para seguir: \n\n[1] - Alta Paciente \n[2] - Alta Turno \n[3] - Modificar Paciente \n[4] - Baja Paciente \n[5] - Lista por dia/mes \n[6] - Lista Pacientes \n[7] - Búsqueda de turnos por DNI \n[8] - Cargar datos de Prueba \n[0] - Cerrar consola\n\n[?] Opcion: "))

                clear()

                break

            else:
                clear()
                print("[!] Uno o ambos datos son incorrectos. Intente nuevamente.\n")
                opcion = int(input("+++ [Sistema Medico] +++\n\n[1] Registro \n[2] Login \n\n[?] Opcion: "))

                while opcion not in [1, 2]:
                    clear()
                    print("[!] Uno o ambos datos ingresados son incorrectos. Intente nuevamente.")
                    print()
                    opcion = int(input("+++ [Sistema Medico] +++\n\n[1] Registro \n[2] Login \n\n[?] Opcion: "))





