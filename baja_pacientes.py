import os

def main():
    def clear():
        os.system("cls")
        print()

    clear()
    a = int(input("[?] Desea dar de baja un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))
    while a == 0:
        dni = input("[?] Ingrese el DNI del paciente a eliminar, por favor: ")
        print()

        f = open("Pacientes.txt", "r")
        for linea in f:
            nombre = linea.split(";")[1]
            if linea.split(";")[0] == dni:
                print(f"[?] Los datos corresponden a {nombre}\n")
                opcion = int(input("[?] ¿Eliminar registro?\n\n[0] = Si \n[1] = No\n\n[+] Opcion: "))
                if opcion == 0:
                    with open('Pacientes.txt', 'r+') as f:
                        content = ''.join(l for l in f if l != linea)
                        f.seek(0)
                        f.write(content)
                        f.truncate()
                        f.close()

                    print("[+] Eliminado con exito")
                    input()

        clear()
        a = int(input("[?] Desea dar de baja un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))

                
if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")
