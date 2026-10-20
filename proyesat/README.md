# Trabajo Práctico — Programación 1
## Seguimiento y caracterización de satélites

Modalidad: grupos de dos personas. Se entrega en dos etapas:

- **Etapa 1** (entrega: viernes 30/10/2026): una foto de todos los satélites en un instante: catálogo, clase `Satelite`, análisis e informe.
- **Etapa 2** (noviembre): los satélites a lo largo del tiempo, y gráficos con Matplotlib. La consigna se publica después de la entrega de la Etapa 1.

## Objetivo

Construir un pequeño paquete de módulos de Python que lea un catálogo de satélites en formato JSON, los agrupe y cuente, calcule la posición de cada satélite, la represente con una clase `Satelite` y genere estadísticas: conteo por tipo de órbita, altitudes por grupo, satélites sobre una zona geográfica.

A diferencia del proyecto anterior, no es un programa de línea de comandos: el código va en módulos `.py` con funciones y clases, y el análisis se presenta en un notebook de Jupyter (`informe.ipynb`) que importa y usa esos módulos.

## Organización requerida

```text
proyecto-satelites/
├── README.md              descripción del repositorio
├── .gitignore
├── funciones_base.py      provisto
├── catalogo.py            lectura del catálogo, grupos y 
|                          lanzamientos por año
├── satelite.py            clase Satelite y crear_satelites
├── analisis.py            conteos, extremos y zonas
├── informe.ipynb          el informe: importa y usa los módulos
├── graficos.py            gráficos (Etapa 2)
├── datos/
│   └── satelites.json     provisto
└── salidas/               figuras generadas (Etapa 2)
```

## Etapa 1

Entrega: viernes 30/10/2026

1. Crear el repositorio del grupo, copiar `funciones_base.py` y `datos/satelites.json`, y armar el ambiente con skyfield siguiendo `instalacion.md`.
2. Crear un `.gitignore` que contenga `.venv/`, `__pycache__/` y `.ipynb_checkpoints/`.
3. Implementar en `catalogo.py` las funciones que trabajan sobre los registros del JSON: lectura, año de lanzamiento, grupos y conteos (ver [El catálogo](#1-el-catálogo-módulo-catalogopy)).
4. Implementar en `satelite.py` la clase `Satelite` y la función `crear_satelites` (ver [La clase `Satelite`](#2-la-clase-satelite-módulo-satelitepy)).
5. Implementar en `analisis.py` las funciones de análisis: conteos, extremos, ordenamiento y satélites en una zona (ver [Funciones de análisis](#3-funciones-de-análisis-módulo-analisispy)).
6. Armar `informe.ipynb` con las secciones pedidas, usando sólo funciones de los módulos (ver [El notebook](#4-el-notebook-informeipynb)).
7. Escribir el `README.md` del repositorio con los integrantes, qué hizo cada uno y cómo correr el proyecto.

El detalle de cada punto está más abajo, en [Detalle de la Etapa 1](#detalle-de-la-etapa-1).

## Etapa 2

Los satélites a lo largo del tiempo (cómo creció su cantidad con los años, la trayectoria de la ISS y sus pases sobre Bariloche, cuántos satélites hay sobre una zona a lo largo de un día) y gráficos con Matplotlib (módulo `graficos.py`). La consigna se publica después de la entrega de la Etapa 1, en noviembre.

---

## Datos

Los datos provienen del repositorio público CelesTrak (<https://celestrak.org/NORAD/elements/>), que publica las órbitas de todos los satélites activos. Para que todos los grupos obtengan los mismos resultados, se usa el archivo provisto `datos/satelites.json`, con 16.710 satélites.

El archivo es una lista de diccionarios, uno por satélite. Por ejemplo, el de la Estación Espacial Internacional:

```json
{
    "OBJECT_NAME": "ISS (ZARYA)",
    "OBJECT_ID": "1998-067A",
    "EPOCH": "2026-10-14T08:06:39.057984",
    "MEAN_MOTION": 15.48861773,
    "ECCENTRICITY": 0.00067245,
    "INCLINATION": 51.6325,
    ...
    "NORAD_CAT_ID": 25544,
    ...
}
```

Sólo vamos a usar dos claves directamente:

| Clave | Contenido | Ejemplo |
|---|---|---|
| `"OBJECT_NAME"` | nombre del satélite | `"ISS (ZARYA)"` |
| `"OBJECT_ID"` | identificador internacional: empieza con el año de lanzamiento | `"1998-067A"` (lanzado en 1998) |

El resto de las claves describen la órbita. No hace falta entenderlas: el diccionario completo se le pasa tal como está a `crear_objeto_skyfield` (ver más abajo), que hace los cálculos.

Las posiciones se calculan para el momento en que corren el notebook:

```python
from datetime import datetime, timezone
ahora = datetime.now(timezone.utc)
```

> Los datos de cada satélite describen su órbita tal como se midió en un momento dado (la clave `"EPOCH"`, que usa `crear_objeto_skyfield`), y a partir de ahí Skyfield calcula la posición en cualquier instante. Pero la órbita real cambia de a poco, y el cálculo se aleja de la realidad a medida que el instante se aleja del `EPOCH`: a unos días el error es de algunos kilómetros, y a semanas o meses puede ser de miles. Con la función `epoch_medio` de `funciones_base.py` pueden ver de qué fecha son los datos y cuántos días pasaron desde entonces.
>
> Un ejemplo es la ISS: el roce con la atmósfera la frena y le hace perder altura de a poco, algunos kilómetros por mes, y cada tanto se encienden motores para volver a subirla (un *reboost*). En <https://heavens-above.com/OrbitHeight.aspx?satid=25544> se ve cómo varió su altura durante el último año: una bajada lenta interrumpida por saltos hacia arriba. Los datos de un `EPOCH` no saben nada de los impulsos que vinieron después, así que un cálculo muy alejado de esa fecha no los tiene en cuenta.
>
> Para los curiosos: en <https://satellitemap.space/> se ven en vivo, sobre un globo terráqueo, las posiciones de Starlink, GPS y miles de otros satélites.
>
> Pueden hacer la prueba: calculen la posición de algunos satélites en un instante muy lejano (dentro de un año, o hace diez) y vean qué pasa con las altitudes y con `crear_satelites`.
>
> Periódicamente vamos a ir renovando el archivo con datos más recientes, para que el momento actual no quede lejos de los `EPOCH`.

---

## Instalación y archivos provistos

Las instrucciones para instalar skyfield y abrir el notebook (desde la terminal o desde VS Code) están en `instalacion.md`.

Se provee el archivo `funciones_base.py`, que no hay que modificar y que hace los cálculos astronómicos con la librería Skyfield:

- `crear_objeto_skyfield(registro)`: recibe el diccionario de un satélite, tal como viene en el JSON, y devuelve el objeto de Skyfield que lo representa. Este objeto sirve para las siguientes funciones:
- `obtener_posicion(objeto_skyfield, momento)`: devuelve una tupla `(latitud, longitud, altitud_km)` en el instante `momento` (un `datetime`).
- `epoch_medio(registros)`: recibe la lista de registros y devuelve como `datetime` (en UTC) la fecha media de sus `"EPOCH"`. Sirve para saber de qué fecha son los datos.
- `obtener_trayectoria(objeto_skyfield, inicio, horas, paso_min)`: devuelve una tupla de tres arrays de numpy `(latitudes, longitudes, altitudes_km)`, con las posiciones cada `paso_min` minutos durante `horas` horas desde `inicio`. Se usa en la Etapa 2.

---

## Detalle de la Etapa 1

### Zonas

Algunas funciones trabajan con una zona: un rectángulo sobre el mapa definido por cuatro números, en este orden: longitud mínima, latitud mínima, longitud máxima y latitud máxima. Se guarda como una tupla, y un satélite está en la zona si su longitud y su latitud están entre esos límites. El borde cuenta como adentro. Por ejemplo, el cuadro centrado en Bariloche:

```python
BARILOCHE = (-76.30, -46.13, -66.30, -36.13)   # lon_min, lat_min, lon_max, lat_max
```

> Para armar otras zonas pueden dibujar un rectángulo sobre el mapa en [bboxfinder](https://bboxfinder.com/#-41.245805,-71.806641,-40.938415,-70.942841). El campo "Box" muestra los cuatro límites en el mismo orden que usamos acá.

### 1. El catálogo (módulo `catalogo.py`)

Funciones que trabajan sobre la lista de diccionarios del JSON (los llamamos registros):

- `leer_satelites(ruta)`: lee el archivo JSON (con codificación `utf-8`) y devuelve la lista de registros. Si el archivo no existe, imprime un aviso y devuelve una lista vacía.
- `anio_lanzamiento(registro)`: devuelve el año de lanzamiento como `int`, a partir de los primeros cuatro caracteres de `"OBJECT_ID"`.
- `grupo(nombre)`: devuelve el grupo al que pertenece un satélite según cómo empieza su nombre, de acuerdo con la tabla de abajo. Si no coincide con ningún prefijo, devuelve `"Otros"`. Conviene guardar la tabla como un diccionario `GRUPOS = {"STARLINK": "Starlink", ...}` al principio del módulo.
- `contar_por_grupo(registros)`: devuelve un diccionario `{grupo: cantidad}`, con la cantidad de satélites de cada grupo.
- `lanzamientos_por_anio(registros)`: devuelve un diccionario `{año: cantidad de satélites lanzados ese año}`.

Grupos:

| El nombre empieza con | Grupo |
|---|---|
| `STARLINK` | `"Starlink"` |
| `ONEWEB` | `"OneWeb"` |
| `KUIPER` | `"Kuiper"` |
| `QIANFAN` | `"Qianfan"` |
| `IRIDIUM` | `"Iridium"` |
| `GLOBALSTAR` | `"Globalstar"` |
| `NAVSTAR` | `"GPS"` |
| `BEIDOU` | `"BeiDou"` |

> Los lanzamientos por año son una estimación: el archivo sólo tiene los satélites que siguen activos hoy. Los que se lanzaron hace años y ya dejaron de funcionar no aparecen, así que la cantidad real lanzada en cada año fue mayor.

### 2. La clase `Satelite` (módulo `satelite.py`)

Una clase muy simple que guarda la posición de un satélite en un instante:

```python
class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""

    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""

    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""

    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""
```

Clasificación por altitud:

| Tipo | Altitud |
|---|---|
| LEO (órbita baja) | menor a 2.000 km |
| MEO (órbita media) | de 2.000 km a menos de 34.000 km |
| GEO (geoestacionaria) | de 34.000 km a 37.000 km |
| HEO (alta / otras) | mayor a 37.000 km |

En el mismo módulo tiene que haber una función que arme los objetos:

```python
def crear_satelites(registros, momento):
    """Devuelve una lista de objetos Satelite con su posición en `momento`."""
```

`crear_satelites` descarta los satélites cuya altitud dé menor a 100 km: son satélites que ya cayeron a la atmósfera y para los que el cálculo da posiciones sin sentido (incluso bajo tierra).

### 3. Funciones de análisis (módulo `analisis.py`)

Sobre una lista de objetos `Satelite`:

- `contar_por_tipo(satelites)`: devuelve un diccionario `{"LEO": n, "MEO": n, "GEO": n, "HEO": n}`, con las cuatro claves siempre presentes (en 0 si no hay satélites de ese tipo).
- `mas_bajo(satelites)` y `mas_alto(satelites)`: devuelven el objeto `Satelite` de menor y de mayor altitud.
- `en_zona(satelites, zona)`: devuelve una lista de los satélites dentro de la zona (usando el método `esta_en_zona`).
- `ordenar_por(satelites, atributo, descendente=False)`: función genérica que devuelve una lista nueva ordenada por cualquier atributo (`"altitud_km"`, `"latitud"`, `"nombre"`, ...). Pista: `sorted` con `key=lambda` y `getattr`.
- `top_n(satelites, n, mas_altos=True)`: devuelve los `n` satélites más altos (o más bajos), reutilizando `ordenar_por`.
- `resumen_por_grupo(satelites)`: usando `grupo` de `catalogo.py`, devuelve un diccionario con un resumen de las altitudes de cada grupo:

```python
{
    "Starlink": {"cantidad": 11125, "minima": 121.0, "media": 470.2, "maxima": 597.2},
    ...
}
```

(Los valores del ejemplo son ilustrativos, porque dependen del momento del cálculo, y están redondeados; la función devuelve los valores sin redondear.)

### 4. El notebook (`informe.ipynb`)

Es el informe del trabajo. Tiene que contener celdas de texto (Markdown) que expliquen lo que se hace y lo que se ve, y celdas de código que sólo importen y llamen a funciones de los módulos.

Secciones mínimas:

1. Carga de datos: cuántos satélites tiene el archivo, de qué fecha son los datos (`epoch_medio`), cuántos días pasaron hasta el momento del cálculo y cuántos satélites descarta `crear_satelites`.
2. Grupos: conteo por grupo. ¿Qué porcentaje del total es Starlink?
3. Lanzamientos por año: cuántos satélites (de los activos hoy) se lanzaron cada año desde 2015. ¿En qué año se lanzaron más?
4. Tipos de órbita: conteo por tipo.
5. Extremos: el más bajo, el más alto y el top 10 de cada uno (imprimir usando `__str__`).
6. Comparación de grupos: una tabla con el resumen de altitudes de cada grupo.
7. Bariloche: cuántos satélites hay en la zona `BARILOCHE` y el listado ordenado de menor a mayor altitud, combinando `en_zona` con `ordenar_por` (imprimir usando `__str__`).
8. Conclusiones: un párrafo que resuma qué grupo predomina, en qué años se lanzaron más satélites, qué tipo de órbita predomina y cuántos satélites hay sobre Bariloche.

---

## Reglas

- En el notebook no se definen funciones ni clases: todo lo reutilizable va en los módulos.
- El notebook tiene que correr de principio a fin sin errores con la opción Restart & Run All del menú Kernel, y se entrega con las salidas guardadas.
- Los módulos no imprimen ni grafican al importarse. Si quieren probar algo dentro de un módulo, usen `if __name__ == "__main__":`.
- Cada función y método lleva un *docstring*.

## Trabajo en grupo

- Repositorio único por grupo, con commits de los dos integrantes. Se revisa con `git log`.
- Una división posible: una persona hace `catalogo.py` y `satelite.py`, la otra `analisis.py`, y el notebook lo hacen entre las dos. Cada una revisa el código de la otra.
- El `README.md` incluye los integrantes, qué hizo cada uno y cómo correr el proyecto.
