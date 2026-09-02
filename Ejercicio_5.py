
print("--- BIENVENIDO A LA ARENA ---")


# ==========================================
# NOMBRE DEL GLADIADOR
# ==========================================

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# ==========================================
# VARIABLES DEL JUEGO
# ==========================================

vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
ataque_enemigo = 12

turno_jugador = True


print("\n=== INICIO DEL COMBATE ===")


# ==========================================
# COMBATE
# ==========================================

while vida_jugador > 0 and vida_enemigo > 0:

    print("\n--------------------------------")
    print(
        nombre,
        "(HP:", vida_jugador,
        ") vs Enemigo (HP:", vida_enemigo,
        ") | Pociones:", pociones
    )
    print("--------------------------------")

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")


    # ======================================
    # VALIDAR OPCIÓN
    # ======================================

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: Ingrese 1, 2 o 3.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)


    # ======================================
    # ATAQUE PESADO
    # ======================================

    if opcion == 1:

        daño = ataque_pesado

        # Golpe crítico
        if vida_enemigo < 20:
            daño = ataque_pesado * 1.5
            print("¡GOLPE CRÍTICO!")

        vida_enemigo = vida_enemigo - daño

        print(
            "¡Atacaste al enemigo por",
            daño,
            "puntos de daño!"
        )


    # ======================================
    # RÁFAGA VELOZ
    # ======================================

    elif opcion == 2:

        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):

            vida_enemigo = vida_enemigo - 5

            print("> Golpe conectado por 5 de daño")

            # Si el enemigo muere durante la ráfaga
            if vida_enemigo <= 0:
                break


    # ======================================
    # CURAR
    # ======================================

    elif opcion == 3:

        if pociones > 0:

            vida_jugador = vida_jugador + 30

            # La vida no puede superar 100
            if vida_jugador > 100:
                vida_jugador = 100

            pociones = pociones - 1

            print("¡Te curaste 30 puntos de vida!")

        else:

            print("¡No quedan pociones!")


    # ======================================
    # COMPROBAR SI EL ENEMIGO MURIÓ
    # ======================================

    if vida_enemigo <= 0:
        break


    # ======================================
    # TURNO DEL ENEMIGO
    # ======================================

    vida_jugador = vida_jugador - ataque_enemigo

    print(
        "¡El enemigo te atacó por",
        ataque_enemigo,
        "puntos de daño!"
    )


# ==========================================
# FIN DEL JUEGO
# ==========================================

print("\n=== FIN DEL COMBATE ===")


if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")

else:
    print("DERROTA. Has caído en combate.")