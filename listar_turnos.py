import os

def clear():
    os.system("cls")
    print()

def listar_turnos(orden=1):
    clear()
    f = open("Turnos.txt", "r")
    listalistas = []
    
    for linea in (f):
        lista = linea[:-1].split(";")
        lista[0], lista[2] = lista[2], lista[0]
        lista[0] = lista[0].split("/")
        if orden == 0:
            lista[0][0], lista[0][1] = lista[0][1], lista[0][0]
        listalistas.append(lista)
        listalistas.sort()

    f.close()
    return listalistas

def main():

    clear()
    opcion = int(input("[?] Como desea obtener el listado de turnos?\n\n[0] Mes\n[1] Dia\n\n[?] Opcion: "))

    if opcion == 0:
        lista = listar_turnos(0)
        clear()
        print("[+] -- Listado por Mes -- [+]\n\n")
        for i in lista:
            print("[+] Fecha del turno: \n")
            print(f"[+] Asociado: {i[2]}\n[+] Hora: {i[1]}\n[+] Dia: {i[0][1]}\n[+] Mes: {i[0][0]}\n[+] Año: {i[0][2]}\n")

    if opcion == 1:
        lista = listar_turnos(1)        
        clear()
        print("[+] -- Listado por Dia -- [+]\n\n")
        for i in lista:
            print("[+] Fecha del turno: \n")
            print(f"[+] Asociado: {i[2]}\n[+] Hora: {i[1]}\n[+] Dia: {i[0][0]}\n[+] Mes: {i[0][1]}\n[+] Año: {i[0][2]}\n")

if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")


