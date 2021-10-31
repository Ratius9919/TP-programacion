import os
from alta_pacientes import main as alta_pacientes

def clear():
    os.system("cls")

def crear_archivo(lista): # Se escribe en el archivo de texto, si no existe se crea.
    try:
        with open("Turnos.txt","a") as turnos:
            turnos.write(f"{lista}\n")
            turnos.close()
    except:
        turnos = open("Turnos.txt","a")
        turnos.write(f"{lista}\n")
        turnos.close()

def leer_archivo_pacientes():
    try:
        f = open ("Pacientes.txt", "r")
        pacientes = f.read()
        f.close()
        return pacientes
    except:
        print("El sistema no tiene ningun paciente subido. Este sera el primero.")
        os.system("pause")
        alta_pacientes()



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


def verificar_dni(dni):
    pacientes = leer_archivo_pacientes()
    ubicacion = str(pacientes).find(str(dni))
    
    if ubicacion == -1:
        print("[+] El paciente no esta dado de alta, se lo redirigira a la pagina de alta.")
        os.system("pause")
        alta_pacientes()
        return True

def crear_dia(): #Se solicita un valor y tras las validaciones para verificar si es un dia, se lo devuelve.
    valor = False
    while valor == False:
        try:
            dia = input("[?] Por favor, ingrese el dia del turno, recuerde que el 1, el 8, el 15 y el 22 el doctor no trabaja: ")
            if int(dia) < 32 and int(dia) > 0 and int(dia) != 1 and int(dia) != 8 and int(dia) != 15 and int(dia) != 22 :
                valor = True
            while int(dia) == 1 or int(dia) == 8 or int(dia) == 15 or int(dia) == 22:
                print("Ingresaste un dia no valido.")
                dia = input("[?] Por favor, ingrese el dia del turno, recuerde que el 1, el 8, el 15 y el 22 el doctor no trabaja: ")
                if int(dia) == 1 or int(dia) == 8 or int(dia) == 15 or int(dia) == 22:
                    valor = True
        except ValueError:
            print("[!] Ingresaste un valor no valido.")
    return dia
    
            

def crear_hora(): #Se solicita un valor y tras las validaciones para verificar si es una hora, se lo devuelve.
    valor = False
    while valor == False:
        try:
            hora = input("[?] Por favor, ingrese la hora del turno, recuerde el horario de atencion es de 10 a 14 hs. Sin los minutos, solo la hora: ")
            if int(hora) >= 10 and int(hora) <= 14:
                valor = True
            else:
                print("Eligio un horario no disponible.")
                hora = input("[?] Por favor, ingrese la hora del turno, recuerde el horario de atencion es de 10 a 14 hs. Sin los minutos, solo la hora: ")
                
        except ValueError:
            print("[!] Ingresaste un valor no valido.")
    
    return hora

def crear_mes():  #Se solicita un valor y tras las validaciones para verificar si es un mes, se lo devuelve.
    valor = False
    while valor == False:
        try:
            mes = input("[?] Por favor, ingrese el mes del turno: ")
            if int(mes) < 13 and int(mes) > 0:
                valor = True
        except ValueError:
            print("[!] Ingresaste un valor no valido.")
    
    return mes

def crear_año():  #Se solicita un valor y tras las validaciones para verificar si es un mes, se lo devuelve.
    valor = False
    
    while valor == False:
        try:
            año = input("[?] Por favor, ingrese el año del turno: ")
            if int(año) >= 2021 :
                valor = True
        except ValueError:
            print("[!] Ingresaste un valor no valido.")    
    return año

def agregar_datos(dato1,dato2,dato3): #Se ingresan los datos dentro de la matriz.
    lista = f"{dato1};{dato2};{dato3}"
    return lista

def opcion_minutos(): #Para simplificar procesos se solicita una A o B para selecciones alguna opcion. 
    clear()
    print("[?] Por favor, solicite cual bloque desea solicitar\n")
    print("[0] - Turno desde el minuto 00 hasta el 30.")
    print("[1] - Turno desde el minuto 30 hasta el 00, de la siguiente hora.\n\n")
    turno = input("[?] Opcion: ")
    if turno == "0" or turno == "1":
        if turno == "0":
            valor = "00"
            return valor
        if turno == "1":
            valor = "30"
            return valor
    else:
        print("[!] Ingresaste un valor no valido. Por favor ingreselo denuevo.")
        opcion_minutos()


def main(): 
    clear()
    a = int(input("[?] Desea dar de alta un turno?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))
    while a == 0:
        #Se crean tres listas, una dentro de la otra. La primera lista almacena el DNI,
        #La segunda almacena la fecha
        #y la tercera almacena la hora del turno
        clear()
        dni = crear_dni()
        valor = verificar_dni(dni)
        if valor == True:
            break
        clear()
        año = crear_año()
        clear()
        mes = crear_mes()
        clear()
        dia = crear_dia()
        clear()
        hora = crear_hora()
        clear()
        minutos = opcion_minutos()
        clear()
        fecha = dia+"/"+mes+"/"+año
        hora_minutos = hora + ":" + minutos
        agregar_datos(hora_minutos,dni,fecha)
        turno = agregar_datos(dni,hora_minutos,fecha)
        print(turno)
        crear_archivo(turno)
        clear()
        a = int(input("[?] Desea dar de alta un turno?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))


main()

