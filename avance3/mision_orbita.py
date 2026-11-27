
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


def autorizar_lanzamiento(disponibles, requeridos):
    # Todos los recursos deben alcanzar el mínimo requerido.
    autorizado = True

    for posicion in range(len(RECURSOS)):
        if disponibles[posicion] < requeridos[posicion]:
            autorizado = False

    return autorizado


# ============================================================
# Componente B: Viaje de ida
# ============================================================

def calcular_consumo_diario(tripulantes):
    # Calcula el consumo diario en el orden de RECURSOS.
    consumo = [
        CONSUMO_COMBUSTIBLE_DIA,
        tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA,
        CONSUMO_ENERGIA_DIA,
        tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA
    ]

    return consumo


def viajar_al_destino(recursos, dias_viaje, tripulantes):
    # Descuenta directamente el consumo total del viaje de ida.
    consumo = calcular_consumo_diario(tripulantes)

    for posicion in range(len(RECURSOS)):
        recursos[posicion] = (
            recursos[posicion]
            - consumo[posicion] * dias_viaje
        )

    return recursos


def recursos_alcanzan(recursos, consumo):
    # Comprueba si todos los recursos alcanzan para un día.
    suficientes = True

    for posicion in range(len(RECURSOS)):
        if recursos[posicion] < consumo[posicion]:
            suficientes = False

    return suficientes


def simular_trayecto(recursos, dias, tripulantes):
    # Inicializa el contador y el control del trayecto.
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True

    # Simula únicamente los días con recursos suficientes.
    while dias_completados < dias and puede_continuar:
        puede_continuar = recursos_alcanzan(
            recursos, consumo
        )

        if puede_continuar:
            for posicion in range(len(RECURSOS)):
                recursos[posicion] = (
                    recursos[posicion] - consumo[posicion]
                )

            dias_completados = dias_completados + 1

            # Presenta los recursos después de cada día.
            print(
                f"Día {dias_completados} | "
                f"Combustible: {recursos[COMBUSTIBLE]} | "
                f"Oxígeno: {recursos[OXIGENO]} | "
                f"Energía: {recursos[ENERGIA]} | "
                f"Provisiones: {recursos[PROVISIONES]}"
            )

    return dias_completados


def mostrar_recursos(recursos):
    # Presenta las cantidades restantes de cada recurso.
    print("Recursos restantes:")

    for posicion in range(len(RECURSOS)):
        print(
            f"- {RECURSOS[posicion].capitalize()}: "
            f"{recursos[posicion]} unidades"
        )



# ============================================================
# Componente C: Exploración con bitácora
# ============================================================

def mostrar_menu_actividades():
    # Presenta las actividades disponibles en la exploración.
    numero = 1

    for actividad in ACTIVIDADES:
        print(f"{numero}. {actividad[ACT_NOMBRE]}")
        numero = numero + 1

    print(f"{len(ACTIVIDADES) + 1}. Finalizar exploración")


def explorar(recursos):
    # La bitácora conserva las actividades en orden de ejecución.
    bitacora = []
    exploracion_activa = True

    while exploracion_activa:
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))

        if opcion == len(ACTIVIDADES) + 1:
            print("Exploración finalizada por la tripulación.")
            exploracion_activa = False

        elif 1 <= opcion <= len(ACTIVIDADES):
            actividad = ACTIVIDADES[opcion - 1]

            # Verifica los recursos antes de realizar la actividad.
            if (
                recursos[COMBUSTIBLE]
                >= actividad[ACT_COMBUSTIBLE]
                and recursos[ENERGIA]
                >= actividad[ACT_ENERGIA]
                and recursos[PROVISIONES]
                >= actividad[ACT_PROVISIONES]
            ):
                recursos[COMBUSTIBLE] = (
                    recursos[COMBUSTIBLE]
                    - actividad[ACT_COMBUSTIBLE]
                )

                recursos[ENERGIA] = (
                    recursos[ENERGIA]
                    - actividad[ACT_ENERGIA]
                )

                recursos[PROVISIONES] = (
                    recursos[PROVISIONES]
                    - actividad[ACT_PROVISIONES]
                )

                # Registra únicamente las actividades completadas.
                bitacora.append([
                    len(bitacora) + 1,
                    actividad[ACT_NOMBRE],
                    actividad[ACT_PUNTOS]
                ])

                print(
                    f"Actividad realizada: "
                    f"{actividad[ACT_NOMBRE]}. "
                    f"Puntos obtenidos: "
                    f"{actividad[ACT_PUNTOS]}"
                )

            else:
                print(
                    "Recursos insuficientes para realizar "
                    "la actividad. La exploración finaliza."
                )
                exploracion_activa = False

        else:
            print("Opción no válida.")

    return bitacora


def contar_actividad(bitacora, nombre_actividad):
    # Cuenta las apariciones de la actividad indicada.
    cantidad = 0

    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            cantidad = cantidad + 1

    return cantidad


def calcular_puntos(bitacora):
    # Acumula los puntos de las actividades completadas.
    puntos = 0

    for fila in bitacora:
        puntos = puntos + fila[BIT_PUNTOS]

    return puntos


def mostrar_resumen_exploracion(bitacora, recursos):
    # Calcula los resultados a partir de la bitácora.
    muestras = contar_actividad(
        bitacora, "Recolectar muestra"
    )

    puntos = calcular_puntos(bitacora)

    print(f"Actividades realizadas: {len(bitacora)}")
    print(f"Muestras recolectadas: {muestras}")
    print(f"Puntos científicos: {puntos}")

    mostrar_recursos(recursos)


