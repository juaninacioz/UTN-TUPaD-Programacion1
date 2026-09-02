# Variables de los turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


# Nombre del operador
operador = input("Nombre del operador: ")

while not operador.isalpha():
    operador = input("Nombre inválido. Ingrese nuevamente: ")


print(f"\nBienvenido/a {operador}")


# MENÚ
while True:

    print("\n===== AGENDA DE TURNOS =====")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    # Validar que sea número
    while not opcion.isdigit():
        opcion = input("Error: ingrese un número válido: ")

    opcion = int(opcion)

    # Validar rango
    while opcion < 1 or opcion > 5:
        opcion = input("Error: opción fuera de rango: ")

        while not opcion.isdigit():
            opcion = input("Error: ingrese un número válido: ")

        opcion = int(opcion)


    # ==========================================
    # 1 - RESERVAR TURNO
    # ==========================================

    if opcion == 1:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día inválido. Ingrese 1 o 2: ")

        dia = int(dia)

        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese nuevamente: ")


        # LUNES
        if dia == 1:

            # Verificar repetido
            if (paciente == lunes1 or
                paciente == lunes2 or
                paciente == lunes3 or
                paciente == lunes4):

                print("Error: el paciente ya tiene un turno ese día.")

            else:

                # Buscar primer espacio libre
                if lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes - Turno 1")

                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes - Turno 2")

                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes - Turno 3")

                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes - Turno 4")

                else:
                    print("No hay turnos disponibles para Lunes.")


        # MARTES
        else:

            # Verificar repetido
            if (paciente == martes1 or
                paciente == martes2 or
                paciente == martes3):

                print("Error: el paciente ya tiene un turno ese día.")

            else:

                # Buscar primer espacio libre
                if martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes - Turno 1")

                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes - Turno 2")

                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes - Turno 3")

                else:
                    print("No hay turnos disponibles para Martes.")


    # ==========================================
    # 2 - CANCELAR TURNO
    # ==========================================

    elif opcion == 2:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día inválido. Ingrese 1 o 2: ")

        dia = int(dia)

        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese nuevamente: ")


        # LUNES
        if dia == 1:

            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado.")

            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado.")

            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado.")

            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado.")

            else:
                print("Paciente no encontrado.")


        # MARTES
        else:

            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado.")

            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado.")

            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado.")

            else:
                print("Paciente no encontrado.")


    # ==========================================
    # 3 - VER AGENDA
    # ==========================================

    elif opcion == 3:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día inválido. Ingrese 1 o 2: ")

        dia = int(dia)


        # LUNES
        if dia == 1:

            print("\n===== AGENDA LUNES =====")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")


        # MARTES
        else:

            print("\n===== AGENDA MARTES =====")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")


    # ==========================================
    # 4 - RESUMEN GENERAL
    # ==========================================

    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        # Contar Lunes
        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1

        # Contar Martes
        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1


        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes


        print("\n===== RESUMEN GENERAL =====")
        print(f"Lunes - Ocupados: {ocupados_lunes} - Disponibles: {disponibles_lunes}")
        print(f"Martes - Ocupados: {ocupados_martes} - Disponibles: {disponibles_martes}")


        # Comparar días
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")

        else:
            print("Día con más turnos: Empate")


    # ==========================================
    # 5 - CERRAR SISTEMA
    # ==========================================

    elif opcion == 5:

        print("Sistema cerrado.")
        break