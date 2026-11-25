
# ============================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Daniel Barboza Álvarez
# Fecha: 25/11/2026
# Versión: 1.0
# Descripción: Sistema integrado Misión Órbita.
# ============================================================

# Declaración de constantes y estructuras de datos

DESTINOS = (
    ("Luna", 3),
    ("Marte", 5),
    ("Europa", 7)
)

ACTIVIDADES = (
    ("Analizar terreno", 0, 8, 0, 10),
    ("Recolectar muestra", 0, 12, 2, 20),
    ("Realizar observación", 0, 5, 0, 8),
    ("Sobrevolar la zona", 15, 3, 0, 25)
)

RECURSOS = (
    "combustible", "oxígeno", "energía", "provisiones"
)

RECURSOS_VITALES = (
    "oxígeno", "energía", "provisiones"
)

RESULTADOS = (
    "Regreso exitoso",
    "Regreso interrumpido",
    "Tripulación varada",
    "No autorizada",
    "No planificada"
)

# Columnas de DESTINOS
DES_NOMBRE = 0
DES_DIAS = 1

# Columnas de ACTIVIDADES
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Posiciones de los recursos
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Columnas de la bitácora
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Columnas del historial de misiones
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# Constantes de consumo diario
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# Constantes de planificación
CANTIDAD_TRAYECTOS = 2
RESERVA_COMBUSTIBLE = 10
RESERVA_OXIGENO = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10


# ============================================================
# Componente A: Preparación y autorización
# ============================================================

def mostrar_destinos():
    # Muestra los destinos disponibles y su duración.
    print("Destinos disponibles:")
    numero = 1

    for destino in DESTINOS:
        print(
            f"{numero}. {destino[DES_NOMBRE]} "
            f"({destino[DES_DIAS]} días)"
        )
        numero = numero + 1


def leer_recursos():
    # Registra los recursos en el orden establecido.
    recursos = []

    for recurso in RECURSOS:
        cantidad = int(
            input(f"Cantidad disponible de {recurso}: ")
        )
        recursos.append(cantidad)

    return recursos


def calcular_requeridos(dias_viaje, tripulantes):
    # Calcula los recursos de ida y regreso,
    # incluyendo las reservas de planificación.
    requeridos = [
        dias_viaje * CONSUMO_COMBUSTIBLE_DIA
        * CANTIDAD_TRAYECTOS + RESERVA_COMBUSTIBLE,

        dias_viaje * CONSUMO_OXIGENO_TRIPULANTE_DIA
        * CANTIDAD_TRAYECTOS * tripulantes
        + RESERVA_OXIGENO,

        dias_viaje * CONSUMO_ENERGIA_DIA
        * CANTIDAD_TRAYECTOS + ENERGIA_EXPLORACION,

        dias_viaje * CONSUMO_PROVISIONES_TRIPULANTE_DIA
        * tripulantes * CANTIDAD_TRAYECTOS
        + PROVISIONES_ADICIONALES
    ]

    return requeridos


def mostrar_resumen(
    nombre_mision, nombre_destino, dias_viaje,
    tripulantes, disponibles, requeridos
):
    # Presenta los datos generales de la misión.
    print(f"Misión: {nombre_mision}")
    print(f"Destino: {nombre_destino}")
    print(f"Duración del viaje de ida: {dias_viaje} días")
    print(f"Tripulantes: {tripulantes}")

    # Compara los recursos disponibles y requeridos.
    for posicion in range(len(RECURSOS)):
        print(
            f"{RECURSOS[posicion].capitalize()}: "
            f"disponible {disponibles[posicion]} | "
            f"requerido {requeridos[posicion]}"
        )

    # Advierte si el margen adicional es bajo.
    margen = (
        disponibles[COMBUSTIBLE]
        - requeridos[COMBUSTIBLE]
    )

    print(
        f"Margen adicional de combustible: "
        f"{margen} unidades"
    )

    if margen < MARGEN_MINIMO_COMBUSTIBLE:
        print(
            "Advertencia: el margen adicional "
            "de combustible es bajo."
        )
