import os

def clear():
    os.system("cls")
    print()

def main():
    clear()
    dni = input("[+] Ingrese su DNI para ver turnos asociados: ")
    
    carpeta = open("Turnos.txt", "r") 
    for i in carpeta:
        lista_turnos = i.split(";")
        doc = lista_turnos[0]
        hora = lista_turnos[1]
        fecha = lista_turnos[2]
        if dni == doc:
            print(f"\n[+] Turno Encontrado:\n\n[+] Documento: {doc}\n[+] Hora: {hora}\n[+] Fecha: {fecha}")
    
    print("[+] Se cargaron todos los turnos encontrados. Continuar..")      
    input()


if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")
