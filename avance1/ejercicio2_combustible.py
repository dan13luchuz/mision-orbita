# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Daniel Barboza Álvarez
# Fecha: 07/10/2026
# Versión: 1.0
# Descripción: Verifica el margen adicional de combustible de una misión.
# ============================================================

# Declaración de constantes
# La reserva se incluye en el combustible total y el margen mínimo
# permite determinar cuándo se debe mostrar una advertencia.
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO = 10

# Entrada de datos
# Se solicitan las cantidades necesarias para verificar el combustible.
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para la ida: "))
combustible_regreso = int(input("Ingrese el combustible requerido para el regreso: "))

# Procesamiento
# Se calcula el combustible necesario para completar toda la misión
# y cuánto queda disponible después de cubrirlo.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# Salida de resultados
# Estas cantidades deben mostrarse siempre, independientemente del margen.
print()
print("Resumen de combustible")
print(f"Combustible disponible: {combustible_disponible} unidades")
print(f"Combustible requerido para llegar: {combustible_ida} unidades")
print(f"Combustible requerido para regresar: {combustible_regreso} unidades")
print(f"Reserva de emergencia: {RESERVA_COMBUSTIBLE} unidades")
print(f"Combustible total requerido: {combustible_total} unidades")
print(f"Combustible adicional disponible: {combustible_adicional} unidades")

# Decisión
# La advertencia aparece únicamente cuando el margen adicional
# es menor que las 10 unidades establecidas.
if combustible_adicional < MARGEN_MINIMO:
    print("Advertencia: el margen adicional de combustible es bajo.")