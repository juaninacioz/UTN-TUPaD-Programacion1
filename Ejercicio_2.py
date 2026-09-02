usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False


# LOGIN
while intentos < 3:

    usuario = input(f"Intento {intentos + 1}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1


# CUENTA BLOQUEADA
if not acceso:
    print("Cuenta bloqueada")


# MENÚ
if acceso:

    while True:

        print("\n1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        # Validar que sea número
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        # Validar rango
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        # Opción 1
        if opcion == 1:
            print("Inscripto")

        # Opción 2
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")

            if len(nueva_clave) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")
                else:
                    print("Error: las claves no coinciden.")

        # Opción 3
        elif opcion == 3:
            print("¡Seguí practicando, cada ejercicio te hace mejor programador!")

        # Opción 4
        elif opcion == 4:
            print("Hasta luego.")
            break