# Trabajo Práctico — Programación 1 (Comisión 2)
## Lectura y caracterización de observaciones meteorológicas del SMN

## Objetivo

Construir una herramienta de línea de comandos que lea el archivo de **observaciones actuales** del Servicio Meteorológico Nacional, lo interprete y guarde los datos en un diccionario indexado por ciudad/estación, y calcule características y estadísticas generales sobre esos datos (estaciones leídas, datos faltantes, columnas ausentes, temperaturas y vientos extremos, rankings de ciudades).

El desafío está en decidir cómo parsear cada línea, cómo representar los datos leídos, cómo informar los problemas encontrados (datos faltantes, columnas ausentes, filas mal formadas) y cómo presentar un resumen claro al finalizar.

La generación de gráficos a partir de estos datos queda para un próximo trabajo práctico.

## De dónde salen los datos

Los datos se obtienen de la página de descarga del SMN:

<https://www.smn.gob.ar/descarga-de-datos>

Ahí se descarga el archivo comprimido (`.rar`) de **observaciones actuales**, se descomprime, y el `.txt` que queda adentro se guarda en la carpeta `datos/` del repositorio. Ese archivo cambia todo el tiempo (son datos en vivo), así que cada grupo va a trabajar con una "foto" distinta según el momento en que lo descargue — está bien que así sea, no hace falta usar siempre el mismo archivo.

## Formato de entrada

El archivo es de texto plano, sin encabezado, con un registro por línea y campos separados por `;`. Por ejemplo:

```text
Azul;10-septiembre-2026;08:00;Algo nublado con neblina;10 km;3.3;1.9; 91;Sur  5;997.7
Bahía Blanca;10-septiembre-2026;08:00;Despejado;15 km;0.4;-3.5; 92;Norte  13;1005
Benito Juárez;09-septiembre-2026;21:00;Despejado;10 km;12.6;No se calcula; 72;Noroeste  3;990.5
```

Los campos, en orden, son:

1. Ciudad / estación
2. Fecha (`dd-mes-aaaa`)
3. Hora
4. Condición del cielo
5. Visibilidad
6. Temperatura (°C)
7. Sensación térmica (°C) — puede venir como el texto `No se calcula` en vez de un número
8. Humedad (%)
9. Viento: dirección y velocidad juntos (por ejemplo `Sur  5`, o `Calma` cuando no hay viento)
10. Presión (hPa)

Puntos a tener en cuenta sobre estos datos reales:

- No todas las estaciones informan a la misma hora: cada ciudad puede tener una fecha/hora de observación distinta dentro del mismo archivo.
- El campo de sensación térmica puede faltar (`No se calcula`): es un caso real de dato faltante que hay que contemplar.
- El campo de viento mezcla dirección y velocidad en un mismo texto (por ejemplo `Norte  3`), y el caso `Calma` no tiene velocidad numérica.
- Los nombres de ciudad pueden traer espacios en blanco de más al principio o al final (arrastrados del archivo original): hay que limpiarlos antes de usarlos como clave del diccionario.

## Comando esperado

```bash
python analisis_smn.py datos/observaciones_smn.txt
```

## Requerimientos

### Lectura y armado del diccionario

- Recibir por argumento la ruta del `.txt` de entrada.
- Leer el archivo completo y guardar los datos en un diccionario, donde cada **clave sea el nombre de la ciudad/estación** (sin espacios en blanco de más) y el **valor sea otro diccionario** con el resto de los campos de esa observación (fecha, hora, condición, temperatura, sensación térmica, humedad, dirección y velocidad del viento, presión).
- El campo de viento debe separarse en **dos campos independientes**: dirección (texto) y velocidad (número). Por ejemplo, `"Norte  3"` se convierte en `direccion_viento = "Norte"` y `velocidad_viento = 3`. El caso `Calma` debe contemplarse (por ejemplo, dirección `"Calma"` y velocidad `0`, o `None`, a criterio del grupo pero documentado).

### Funciones de caracterización

A partir del diccionario armado, se deben implementar funciones para obtener:

- cantidad total de ciudades leídas;
- cantidad de ciudades con **todos** los datos completos (sin ningún campo faltante, por ejemplo sin `No se calcula` en sensación térmica);
- columnas/campos esperados que no están presentes en alguna línea, comparando contra la lista de campos definida arriba;
- cantidad de datos faltantes por campo, y en qué estaciones ocurre;
- ciudad(es) con la **temperatura máxima** y con la **temperatura mínima**;
- ciudad(es) con la **velocidad de viento máxima** y con la **mínima**;
- listado de las **n ciudades más cálidas** (temperatura más alta primero), donde `n` es un parámetro de la función;
- listado de las **n ciudades más frías**;
- listado de las **n ciudades con más viento**;
- listado de las **n ciudades con menos viento**.

Estas cuatro últimas funciones de listado deben poder reutilizarse tanto para temperatura como para viento (por ejemplo, con una función genérica que reciba por parámetro qué campo ordenar, en lugar de duplicar el código four veces).

### Presentación

- Mostrar por pantalla un resumen legible con todo lo anterior al finalizar la ejecución.
- Manejar errores de argumentos y de lectura del archivo (archivo inexistente, vacío, línea mal formada) con mensajes claros, sin que el programa se corte de forma abrupta.
- Dividir el programa en funciones con una responsabilidad clara cada una (lectura, cada cálculo, presentación del resumen), evitando una única función que haga todo.

## Encabezados de funciones sugeridos

Como guía para organizar el programa, se sugieren las siguientes funciones. No es obligatorio usar exactamente estos nombres, pero sí se espera una división de responsabilidades equivalente (no todo resuelto en una sola función).

```python

def leer_observaciones(ruta: str) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""

def separar_viento(campo_viento: str) -> tuple:
    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""


def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""


def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""


def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    como para viento."""


def mostrar_resumen(observaciones: dict) -> None:
    """Imprime por pantalla el resumen con todas las características calculadas. Usar n=5"""

```

## Validaciones mínimas

- Las líneas con una cantidad de campos distinta a la esperada (10) se consideran inválidas y se cuentan aparte (no rompen la lectura del resto del archivo).
- Un valor `No se calcula` en sensación térmica se considera dato faltante, no un error de formato — no debe romper la conversión a número del resto del programa.
- Los nombres de ciudad se deben limpiar de espacios en blanco sobrantes antes de usarlos como clave del diccionario.
- El campo de viento debe poder separarse en dirección y velocidad; el caso `Calma` (sin velocidad numérica) debe contemplarse sin que el programa falle.

## Documentación

El proyecto debe incluir un `README.md` con: descripción breve del proyecto, cómo ejecutarlo, cómo se consigue el archivo de entrada (link a la página del SMN y pasos para descomprimir el `.rar`), y un ejemplo de la salida por consola.

## Estructura del repositorio

Por ahora, sin separar en subcarpetas de código ni tests:

```
nombre-proyecto/
├── README.md
├── analisis_smn.py
├── (otros .py si dividen el programa en módulos)
├── datos/
│   └── observaciones_smn.txt
└── .gitignore
```

El testing y la generación de gráficos se dejan para una etapa posterior del proyecto.

## Historial de commits — mención especial

Esta parte se evalúa tanto como el código:

- **Commits frecuentes y atómicos**: cada commit debe representar un paso de trabajo identificable (ej: "agrego lectura del txt a diccionario", "agrego separación de dirección y velocidad del viento", "agrego ranking de ciudades más cálidas"), no un volcado único de todo el proyecto.
- **Mensajes de commit descriptivos**, en modo imperativo o presente ("agrega", "corrige", "refactoriza"), no genéricos ("cambios", "update").
- **Fechas de los commits**: deben reflejar el proceso real de trabajo, distribuido en el tiempo (no todos el mismo día/hora antes de la entrega). Se va a revisar `git log` para ver la evolución.
- Se puede usar `git log --oneline --graph --date=short --pretty=format:"%h %ad %s"` para revisar esto antes de entregar.
