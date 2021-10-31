import os



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

def escribir_archivo(lista):
    
    with open("Pacientes.txt","a") as pacientes:
        pacientes.write(f"{lista}\n")
     


def leer_archivo():
    f = open ("Pacientes.txt", "r")
    paciente = f.read()
    f.close()
    return paciente

def borrar_archivo():
    with open("Pacientes.txt","a") as pacientes:
        pacientes.truncate(0)

def lista():
    pacientes = leer_archivo()
    listar = pacientes.split("\n")  
    return listar

def buscar_dni(dni):
    
    lista_pacientes = lista()
    for i in range (len(lista_pacientes)):
        paciente = lista_pacientes[i]
        buscar = paciente.find(dni)
        if buscar != -1:
            
            return i
        elif buscar == -1:
            return buscar

def modificar_paciente(dni):
    
    ubicacion = buscar_dni(dni)
    if ubicacion == -1:
        return -1
    lista_pacientes = lista()
        
    lista_paciente= lista_pacientes[ubicacion].split(";")
    
        
    pregunta = int(input("[?] Que desea cambiar? [1] El DNI. [2] El nombre. [3] la edad. [0] Todos. [-1] Nada."))
    if pregunta == 1:
        lista_pacientes = lista_pacientes.pop(ubicacion)
        lista_paciente[pregunta-1] = crear_dni()
            
    if pregunta == 2:
        lista_pacientes = lista_pacientes.pop(ubicacion)
        nombre = input("[?] Ingrese su nombre por favor: ")
        while nombre.isdigit():
            nombre = input("[?] Ingrese su nombre por favor, solo letras: ")
        lista_paciente[pregunta-1] = nombre
        
    if pregunta == 3:
        lista_pacientes = lista_pacientes.pop(ubicacion)
        edad = input("[?] Edad: ")
        while edad.isdigit() == False:
            edad = input("[?] Ingrese su edad nuevamente. Solo numeros: ")
        while int(edad) <= 17:
            print("[!] Error, no se le puede inscribir si es menor de 17.")
            edad = input("[?] Ingrese su edad nuevamente: ")
        lista_paciente[pregunta-1] = edad
    


    if pregunta == 0:
        lista_pacientes = lista_pacientes.pop(ubicacion)
        lista_paciente[0] = crear_dni()
        nombre = input("[?] Ingrese su nombre por favor: ")
        while nombre.isdigit():
            nombre = input("[?] Ingrese su nombre por favor, solo letras: ")
        lista_paciente[1] = nombre
        edad = input("[?] Edad: ")
        while edad.isdigit() == False:
            edad = input("[?] Ingrese su edad nuevamente. Solo numeros: ")
        while int(edad) <= 17:
            print("[!] Error, no se le puede inscribir si es menor de 17.")
            edad = input("[?] Ingrese su edad nuevamente: ")
        lista_paciente[2] = edad
    return lista_paciente

def modificar_lista(dni):
    valor = modificar_paciente(dni)
    if valor == -1:
        print("[!] No se ha encontrado el DNI, volviendo a la pantalla anterior.")
        return
    lista_original = lista()
    ubicacion = buscar_dni(dni)
    lista_original.pop(ubicacion)
    lista_original.insert(ubicacion,valor)
    lista_str = str(lista_original)
    lista_str.replace("["," ")
    lista_str.replace("]"," ")
    lista_str.replace("'"," ")

    return lista_original

def main(dni):
    valor = buscar_dni(dni)
    if valor == -1:
        return
    lista = modificar_lista(dni)
    borrar_archivo()
    escribir_archivo(lista)


dni = input("¿Cual es el DNI que desea modificar?")
main(dni)