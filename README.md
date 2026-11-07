# Misión Órbita

Proyecto del curso **Principios de Programación 1**, desarrollado progresivamente en Python mediante programas independientes relacionados con la preparación y ejecución de una misión de exploración espacial.

## Integrante

- Daniel Barboza Álvarez

## Curso

**SOFT-01 - Principios de Programación 1**  
Sección SCV3  
Periodo C3-2026

## Descripción

Misión Órbita es un simulador básico de exploración espacial desarrollado en Python.

El proyecto se construye mediante diferentes avances. En el **primer avance** se trabajó la preparación de la misión, incluyendo el cálculo y verificación de recursos y la autorización del lanzamiento.

En el **segundo avance** se trabaja la ejecución de la misión mediante estructuras condicionales e iterativas, contadores, acumuladores y variables de control. Al desarrollarse este avance de forma individual, corresponden los ejercicios 7 y 8.

## Estructura del proyecto

```text
mision-orbita/
├── README.md
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
├── avance2/
│   ├── ejercicio7_exploracion.py
│   └── ejercicio8_regreso.py
└── documentacion/
    ├── avance1.pdf
    ├── Ejercicio7_Exploracion.pdf
    └── Ejercicio8_Regreso.pdf
```

## Avance 1: Preparación de la misión

### Ejercicio 1 — Cálculo de recursos necesarios

Calcula los recursos necesarios para una misión considerando combustible de ida y regreso, reserva de combustible, oxígeno, energía y provisiones.

### Ejercicio 2 — Verificación de combustible

Calcula el combustible total requerido y verifica el combustible adicional disponible para la misión.

### Ejercicio 3 — Verificación del soporte para la tripulación

Comprueba si el oxígeno y las provisiones disponibles son suficientes para la tripulación.

### Ejercicio 4 — Autorización inicial de lanzamiento

Evalúa combustible, oxígeno, energía y provisiones para determinar si el lanzamiento puede ser autorizado.

## Avance 2: Ejecución de la misión

### Ejercicio 7 — Actividades de exploración científica

Simula la etapa de exploración mediante un menú repetitivo de actividades.

El programa permite:

- Analizar terreno.
- Recolectar muestras.
- Realizar observaciones.
- Finalizar voluntariamente la exploración.
- Verificar la energía y las provisiones antes de realizar cada actividad.
- Acumular puntos científicos.
- Contar las actividades realizadas y las muestras recolectadas.
- Finalizar la exploración cuando los recursos son insuficientes.

### Ejercicio 8 — Evaluación del regreso y supervivencia de la tripulación

Evalúa el estado de la nave al finalizar la exploración.

El programa contempla dos situaciones:

- **Regreso a la Tierra:** si existe combustible suficiente, se simula el viaje de regreso día por día y se actualizan los recursos disponibles.
- **Tripulación varada:** si no existe combustible suficiente para iniciar el regreso, se calculan los días de supervivencia según oxígeno, energía y provisiones y se identifica el recurso o los recursos limitantes.

## Ejecución

1. Tener Python instalado en el equipo.
2. Abrir el repositorio `mision-orbita` en Visual Studio Code.
3. Abrir la carpeta correspondiente al avance.
4. Seleccionar el archivo `.py` que se desea ejecutar.
5. Ejecutar el programa con Python.
6. Ingresar en la terminal los datos solicitados.

Cada ejercicio se ejecuta de forma independiente.

## Convenciones y estilo de programación

- Los nombres de variables se escriben en `snake_case`.
- Las constantes se escriben en MAYÚSCULAS.
- Se utiliza una indentación de 4 espacios.
- Los nombres utilizados buscan describir claramente el propósito de cada variable.
- Cada archivo contiene un encabezado con información del programa.
- Los bloques principales del código incluyen comentarios explicativos.
- Los programas utilizan únicamente la consola para entrada y salida de datos.
- Cada ejercicio se mantiene en un archivo `.py` independiente.
- Los ciclos terminan mediante sus propias condiciones y variables de control.
- No se utilizan funciones propias, colecciones ni librerías externas en los ejercicios del segundo avance.

## Retroalimentación del Avance 1

En la evaluación del primer avance no se indicaron observaciones correctivas específicas. Por esta razón, no fue necesario aplicar correcciones derivadas de la retroalimentación docente.

| Observación del docente | Corrección aplicada | Commit |
| --- | --- | --- |
| No se indicaron observaciones correctivas en la evaluación del Avance 1. | No aplica. No se requirieron correcciones. | No aplica |