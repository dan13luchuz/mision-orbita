# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Daniel Barboza Álvarez
# Fecha: 07/10/2026
# Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# Declaración de constantes
# Estos valores representan los consumos y reservas establecidos
# para realizar los cálculos de la misión.
CONSUMO_COMBUSTIBLE = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3

# Entrada de datos
# Se solicitan los datos básicos necesarios para calcular los recursos.
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de días hasta el destino: "))

# Procesamiento
# Se calcula el combustible necesario para el viaje de ida y regreso.
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Se calculan los recursos considerando el viaje de ida y regreso.
oxigeno_requerido = dias_viaje * CONSUMO_OXIGENO * tripulantes * 2 + RESERVA_OXIGENO
energia_requerida = dias_viaje * CONSUMO_ENERGIA * 2 + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * tripulantes * 2 + PROVISIONES_ADICIONALES

# Salida de resultados
# Se muestra el resumen completo de los recursos necesarios para la misión.
print()
print("Resumen de la misión")
print(f"Misión: {nombre_mision}")
print(f"Tripulantes: {tripulantes}")
print(f"Duración estimada hasta el destino: {dias_viaje} día(s)")
print(f"Combustible para llegar: {combustible_ida} unidades")
print(f"Combustible para regresar: {combustible_regreso} unidades")
print(f"Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades")
print(f"Combustible total requerido: {combustible_total} unidades")
print(f"Oxígeno requerido: {oxigeno_requerido} unidades")
print(f"Energía requerida: {energia_requerida} unidades")
print(f"Provisiones requeridas: {provisiones_requeridas} unidades")