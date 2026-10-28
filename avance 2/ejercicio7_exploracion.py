# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Daniel Barboza Álvarez
# Fecha: 28/10/2026
# Versión: 1.0
# Descripción: Simula las actividades de exploración científica.
# ============================================================

# Declaración de constantes
ENERGIA_ANALIZAR_TERRENO = 8
PUNTOS_ANALIZAR_TERRENO = 10

ENERGIA_RECOLECTAR_MUESTRA = 12
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_RECOLECTAR_MUESTRA = 20

ENERGIA_REALIZAR_OBSERVACION = 5
PUNTOS_REALIZAR_OBSERVACION = 8

# Entrada de datos
energia_disponible = int(input("Ingrese la energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles al llegar al destino: "))

# Inicialización de contadores, acumulador y variable de control
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
exploracion_activa = True

# Ciclo principal de exploración
while exploracion_activa:
    print("\n1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione una actividad: "))

    # Selección de la actividad
    if opcion == 1:
        nombre_actividad = "Analizar terreno"
        energia_actividad = ENERGIA_ANALIZAR_TERRENO
        provisiones_actividad = 0
        puntos_actividad = PUNTOS_ANALIZAR_TERRENO

    elif opcion == 2:
        nombre_actividad = "Recolectar muestra"
        energia_actividad = ENERGIA_RECOLECTAR_MUESTRA
        provisiones_actividad = PROVISIONES_RECOLECTAR_MUESTRA
        puntos_actividad = PUNTOS_RECOLECTAR_MUESTRA

    elif opcion == 3:
        nombre_actividad = "Realizar observación"
        energia_actividad = ENERGIA_REALIZAR_OBSERVACION
        provisiones_actividad = 0
        puntos_actividad = PUNTOS_REALIZAR_OBSERVACION

    elif opcion == 4:
        print("Exploración finalizada por la tripulación.")
        exploracion_activa = False

    else:
        print("Opción no válida.")

    # Procesamiento de las actividades 1, 2 y 3
    if opcion >= 1 and opcion <= 3 and exploracion_activa:
        if (
            energia_disponible >= energia_actividad
            and provisiones_disponibles >= provisiones_actividad
        ):
            energia_disponible = energia_disponible - energia_actividad
            provisiones_disponibles = provisiones_disponibles - provisiones_actividad

            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad

            if opcion == 2:
                muestras_recolectadas = muestras_recolectadas + 1

            print(
                f"Actividad realizada: {nombre_actividad}. "
                f"Puntos obtenidos: {puntos_actividad}"
            )

        else:
            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )
            exploracion_activa = False

# Salida de resultados
print("\nResumen de exploración")
print(f"Actividades realizadas: {actividades_realizadas}")
print(f"Muestras recolectadas: {muestras_recolectadas}")
print(f"Puntos científicos: {puntos_cientificos}")
print(f"Energía restante: {energia_disponible} unidades")
print(f"Provisiones restantes: {provisiones_disponibles} unidades")