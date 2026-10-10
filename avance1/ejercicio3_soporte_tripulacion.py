# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Daniel Barboza Álvarez
# Fecha: 09/10/2026
# Versión: 1.0
# Descripción: Verifica si la nave posee recursos suficientes para la tripulación.
# ============================================================

# Entrada de datos
# Se solicitan los recursos disponibles y requeridos para la misión.
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# Proceso y salida
# Se verifica si la nave cuenta con oxígeno y provisiones suficientes.
print()
print("Verificación del soporte para la tripulación")

if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")