# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Daniel Barboza Álvarez
# Fecha: 29/10/2026
# Versión: 1.0
# Descripción: Simula el regreso de la tripulación a la Tierra.
# ============================================================

# Declaración de constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# Entrada de datos
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje_ida = int(input("Ingrese la cantidad de días del viaje de ida: "))
combustible_disponible = int(input("Ingrese el combustible disponible: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# Cálculo del combustible necesario para realizar el regreso
combustible_necesario_regreso = (
    dias_viaje_ida * CONSUMO_COMBUSTIBLE_DIA
)

# Cálculo de los consumos diarios de la tripulación
consumo_oxigeno_dia = (
    tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA
)

consumo_provisiones_dia = (
    tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA
)

# Caso A: la nave inicia el regreso cuando posee
# combustible suficiente para completar todos los días.
if combustible_disponible >= combustible_necesario_regreso:
    dias_completados = 0
    regreso_activo = True

    # Cada repetición representa un día del viaje de regreso.
    while dias_completados < dias_viaje_ida and regreso_activo:

        # Los recursos se verifican antes de realizar el consumo.
        if (
            combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA
            and oxigeno_disponible >= consumo_oxigeno_dia
            and energia_disponible >= CONSUMO_ENERGIA_DIA
            and provisiones_disponibles >= consumo_provisiones_dia
        ):
            combustible_disponible = (
                combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
            )

            oxigeno_disponible = (
                oxigeno_disponible - consumo_oxigeno_dia
            )

            energia_disponible = (
                energia_disponible - CONSUMO_ENERGIA_DIA
            )

            provisiones_disponibles = (
                provisiones_disponibles - consumo_provisiones_dia
            )

            dias_completados = dias_completados + 1

            print(
                f"Día {dias_completados} | "
                f"Combustible: {combustible_disponible} | "
                f"Oxígeno: {oxigeno_disponible} | "
                f"Energía: {energia_disponible} | "
                f"Provisiones: {provisiones_disponibles}"
            )

        else:
            regreso_activo = False

    # Resultado final del regreso
    if dias_completados == dias_viaje_ida:
        print("La tripulación regresó exitosamente a la Tierra.")
        print(
            f"Combustible restante: "
            f"{combustible_disponible} unidades"
        )
        print(
            f"Oxígeno restante: "
            f"{oxigeno_disponible} unidades"
        )
        print(
            f"Energía restante: "
            f"{energia_disponible} unidades"
        )
        print(
            f"Provisiones restantes: "
            f"{provisiones_disponibles} unidades"
        )

    else:
        dia_interrumpido = dias_completados + 1

        print(
            f"El regreso se interrumpió en el día "
            f"{dia_interrumpido}."
        )

        # El combustible no se incluye porque ya se verificó
        # que alcanza para completar el regreso.
        if oxigeno_disponible < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")

        if energia_disponible < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")

        if provisiones_disponibles < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")

        print("La tripulación no completó el regreso.")

# El Caso B se implementará en la siguiente etapa del desarrollo.