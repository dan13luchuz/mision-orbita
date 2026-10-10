# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Daniel Barboza Álvarez
# Fecha: 10/10/2026
# Versión: 1.0
# Descripción: Verifica si una misión puede ser autorizada para el lanzamiento.
# ============================================================

# Declaración de constante
# Se establece la reserva de combustible requerida para la misión.
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
# Se solicitan los recursos disponibles y requeridos para la misión.
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para la ida: "))
combustible_regreso = int(input("Ingrese el combustible requerido para el regreso: "))

oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))

energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))

provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# Procesamiento
# Se calcula el combustible total requerido incluyendo la reserva.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Decisión y salida
# El lanzamiento solamente se autoriza si todos los recursos son suficientes.
print()
print("Verificación para el lanzamiento")

if (
    combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas
):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")