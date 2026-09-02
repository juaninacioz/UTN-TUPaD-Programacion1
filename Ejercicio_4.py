energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre = input("Nombre del agente: ")

while not nombre.isalpha():
    nombre = input("Error. Ingrese solo letras: ")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print("\n-------------------------")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("-------------------------")

    # Bloqueo por alarma
    if alarma and tiempo <= 3:
        print("La alarma bloqueo la boveda.")
        break

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opcion: ")

    while not opcion.isdigit():
        opcion = input("Error. Ingrese un numero: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        opcion = input("Error. Ingrese 1, 2 o 3: ")

        while not opcion.isdigit():
            opcion = input("Error. Ingrese un numero: ")

        opcion = int(opcion)


    # FORZAR CERRADURA
    if opcion == 1:

        energia = energia - 20
        tiempo = tiempo - 2
        forzar_seguidas = forzar_seguidas + 1

        print("Intentando forzar cerradura...")

        # Tres veces seguidas
        if forzar_seguidas == 3:

            alarma = True
            print("La cerradura se trabo.")
            print("ALARMA ACTIVADA.")

        else:

            # Riesgo de alarma
            if energia < 40:

                numero = input("Ingrese un numero del 1 al 3: ")

                while not numero.isdigit():
                    numero = input("Ingrese un numero del 1 al 3: ")

                numero = int(numero)

                while numero < 1 or numero > 3:
                    numero = input("Ingrese un numero del 1 al 3: ")

                    while not numero.isdigit():
                        numero = input("Ingrese un numero del 1 al 3: ")

                    numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("ALARMA ACTIVADA.")

            if not alarma:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("Cerradura abierta.")


    # HACKEAR PANEL
    elif opcion == 2:

        energia = energia - 10
        tiempo = tiempo - 3

        # Se corta la racha
        forzar_seguidas = 0

        print("Hackeando panel...")

        for i in range(4):
            codigo_parcial = codigo_parcial + "A"
            print("Paso", i + 1, "- Codigo:", codigo_parcial)

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("Codigo completo. Cerradura abierta.")
        else:
            print("El codigo todavia esta incompleto.")


    # DESCANSAR
    elif opcion == 3:

        energia = energia + 15

        if energia > 100:
            energia = 100

        tiempo = tiempo - 1

        # Se corta la racha
        forzar_seguidas = 0

        if alarma:
            energia = energia - 10

        print("Descansaste.")
        print("Energia:", energia)


# FIN DEL JUEGO

if cerraduras_abiertas == 3:
    print("\nVICTORIA")
    print("Abriste las 3 cerraduras.")

elif energia <= 0:
    print("\nDERROTA")
    print("Te quedaste sin energia.")

elif tiempo <= 0:
    print("\nDERROTA")
    print("Te quedaste sin tiempo.")

elif alarma and tiempo <= 3:
    print("\nDERROTA")
    print("La boveda se bloqueo por la alarma.")