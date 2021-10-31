import os

def clear():
    os.system("cls")
    print()

def crear_archivo(info): # Se escribe en el archivo de texto, si no existe se crea.
    try:
        with open("Pacientes.txt","a") as turnos:
            turnos.write(f"{info}\n")
            turnos.close()
    except:
        turnos = open("Pacientes.txt","a")
        turnos.write(f"{info}\n")
        turnos.close()

def crear_dni(): #Se solicita un valor y tras las validaciones para verificar si es un dni, se lo devuelve.
    valor = False
    while valor == False:
        try:
            dni = input("[?] Por favor, ingrese su DNI: ")
            
            if int(dni) > 1000000 and int(dni) < 200000000:
                valor = True
        except ValueError:
            print("[!] Ingresaste un valor no valido.")
    return dni

def main():
    clear()
    a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))
    while a == 0:

        dni = crear_dni()
        
        
        nombre = input("[?] Ingrese su nombre por favor: ")
        while nombre.isdigit():
            nombre = input("[?] Ingrese su nombre por favor, solo letras: ")

        edad = input("[?] Edad: ")
        while edad.isdigit() == False:
            edad = input("[?] Ingrese su edad nuevamente. Solo numeros: ")
        while int(edad) <= 17:
            print("[!] Error, no se le puede inscribir si es menor de 17.")
            edad = input("[?] Ingrese su edad nuevamente: ")


        l = f"{dni};{nombre};{edad}"

        crear_archivo(l)

        print()
        clear()
        return

