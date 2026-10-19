# Trabajo Práctico — Programación 1
## Seguimiento y caracterización de satélites

Modalidad: grupos de dos personas. Fecha de entrega: a definir.

## Objetivo

Construir un pequeño paquete de módulos de Python que lea un catálogo de satélites en formato JSON, los agrupe y cuente, estime cómo creció la cantidad de satélites a lo largo de los años, calcule la posición de cada satélite en un instante o en un rango de tiempo, la represente con una clase `Satelite`, genere estadísticas (conteo por tipo de órbita, satélites sobre una zona geográfica, pases sobre una ciudad, evolución a lo largo de un día) y visualice los resultados con Matplotlib.

A diferencia del proyecto anterior, no es un programa de línea de comandos: el código va en módulos `.py` con funciones y clases, y el análisis se presenta en un notebook de Jupyter (`informe.ipynb`) que importa y usa esos módulos.

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

Salvo que se indique otra cosa, todos los cálculos de posición se hacen para la fecha de referencia:

```python
from datetime import datetime, timezone
FECHA_REF = datetime(2026, 10, 19, 12, 0, tzinfo=timezone.utc)
```

---

## Instalación y archivos provistos

Las instrucciones para instalar skyfield y abrir el notebook (desde la terminal o desde VS Code) están en `instalacion.md`.

Se proveen dos archivos que no hay que modificar: `tests.py` (ver Reglas) y `funciones_base.py`, que hace los cálculos astronómicos con la librería Skyfield:

- `crear_objeto_skyfield(registro)`: recibe el diccionario de un satélite, tal como viene en el JSON, y devuelve el objeto de Skyfield que lo representa. Este objeto sirve para las siguientes funciones:
- `obtener_posicion(objeto_skyfield, momento)`: devuelve una tupla `(latitud, longitud, altitud_km)` en el instante `momento` (un `datetime`).
- `obtener_trayectoria(objeto_skyfield, inicio, horas, paso_min)`: devuelve una tupla de tres arrays de numpy `(latitudes, longitudes, altitudes_km)`, con las posiciones cada `paso_min` minutos durante `horas` horas desde `inicio` (en el notebook, normalmente `FECHA_REF`). Cada array tiene `horas * 60 // paso_min` elementos. Es mucho más rápida que llamar a `obtener_posicion` en un ciclo.

---

## Requerimientos

### 1. El catálogo (módulo `catalogo.py`)

Funciones que trabajan sobre la lista de diccionarios del JSON (los llamamos registros):

- `leer_satelites(ruta)`: lee el archivo JSON (con codificación `utf-8`) y devuelve la lista de registros. Si el archivo no existe, imprime un aviso y devuelve una lista vacía.
- `anio_lanzamiento(registro)`: devuelve el año de lanzamiento como `int`, a partir de los primeros cuatro caracteres de `"OBJECT_ID"`.
- `grupo(nombre)`: devuelve el grupo al que pertenece un satélite según cómo empieza su nombre, de acuerdo con la tabla de abajo. Si no coincide con ningún prefijo, devuelve `"Otros"`. Conviene guardar la tabla como un diccionario `GRUPOS = {"STARLINK": "Starlink", ...}` al principio del módulo.
- `contar_por_grupo(registros)`: devuelve un diccionario `{grupo: cantidad}`, ordenado de mayor a menor cantidad.
- `filtrar_por_grupo(registros, nombre_grupo)`: devuelve la lista de los registros de ese grupo.
- `lanzamientos_por_anio(registros)`: devuelve un diccionario `{año: cantidad de satélites lanzados ese año}`, con las claves ordenadas de menor a mayor.
- `linea_de_tiempo(registros, desde, hasta)`: devuelve una tupla de dos arrays de numpy `(anios, acumulado)`. `anios` tiene todos los años de `desde` a `hasta`, incluidos los dos, y `acumulado` la cantidad total de satélites lanzados hasta ese año inclusive. Los años sin lanzamientos repiten el valor del año anterior. Pista: armar primero un array con la cantidad de cada año (0 si no hubo lanzamientos) y usar `np.cumsum`.
- `cargar_objetos(registros)`: devuelve un diccionario `{nombre: objeto_skyfield}`, usando `crear_objeto_skyfield`.

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

> La línea de tiempo es una estimación: el archivo sólo tiene los satélites que siguen activos hoy. Los que se lanzaron hace años y ya dejaron de funcionar no aparecen, así que la cantidad real en cada año fue mayor.

### 2. La clase `Satelite` (módulo `satelite.py`)

Una clase muy simple que guarda la posición de un satélite en un instante:

```python
class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""

    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""

    def esta_en_region(self, lat, lon, delta):
        """True si el satélite está dentro de [lat - delta, lat + delta] x [lon - delta, lon + delta]."""

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

`crear_satelites` descarta los satélites cuya altitud dé menor a 100 km: son satélites que ya cayeron a la atmósfera y para los que el cálculo da posiciones sin sentido (incluso bajo tierra). Con `datos/satelites.json` se descartan 2.

### 3. Funciones de análisis (módulo `analisis.py`)

Sobre una lista de objetos `Satelite`:

- `contar_por_tipo(satelites)`: devuelve un diccionario `{"LEO": n, "MEO": n, "GEO": n, "HEO": n}`, con las cuatro claves siempre presentes (en 0 si no hay satélites de ese tipo).
- `mas_bajo(satelites)` y `mas_alto(satelites)`: devuelven el objeto `Satelite` de menor y de mayor altitud.
- `en_region(satelites, lat, lon, delta)`: devuelve una lista de los satélites dentro del cuadro (usando el método `esta_en_region`).
- `ordenar_por(satelites, atributo, descendente=False)`: función genérica que devuelve una lista nueva ordenada por cualquier atributo (`"altitud_km"`, `"latitud"`, `"nombre"`, ...). Pista: `sorted` con `key=lambda` y `getattr`.
- `top_n(satelites, n, mas_altos=True)`: devuelve los `n` satélites más altos (o más bajos), reutilizando `ordenar_por`.
- `a_diccionario(satelites)`: devuelve la misma información como diccionario de diccionarios:

```python
{
    "ISS (ZARYA)": {
        "latitud": 2.1503,
        "longitud": -161.3743,
        "altitud_km": 419.72,
        "tipo_orbita": "LEO"
    },
    ...
}
```

- `resumen_por_grupo(satelites)`: usando `grupo` de `catalogo.py`, devuelve un diccionario con un resumen de las altitudes de cada grupo:

```python
{
    "Starlink": {"cantidad": 11125, "minima": 121.0, "media": 470.2, "maxima": 597.2},
    ...
}
```

(En el ejemplo los valores están redondeados; la función devuelve los valores sin redondear.)

Sobre un rango de tiempo (reciben objetos de Skyfield, no objetos `Satelite`):

- `trayectoria(objeto_skyfield, inicio, horas, paso_min)`: devuelve una lista de tuplas `(momento, latitud, longitud, altitud_km)` cada `paso_min` minutos durante `horas` horas, usando `obtener_posicion`. La primera tupla corresponde a `inicio` y la lista tiene `horas * 60 // paso_min` elementos (por ejemplo, 3 horas con paso de 1 minuto dan 180 posiciones). Pista: `timedelta(minutes=...)`.
- `pases_sobre(objeto_skyfield, lat, lon, delta, inicio, horas)`: devuelve una lista de pases: cada pase es una tupla `(momento_entrada, momento_salida)`, con el primer y el último minuto en que el satélite está dentro del cuadro. Se recorre la trayectoria minuto a minuto, y minutos consecutivos dentro del cuadro forman un único pase. Como referencia, con `FECHA_REF` como inicio, la ISS tiene 5 pases en 24 h por el cuadro de Bariloche con `delta = 10`.
- `en_region_en_el_tiempo(objetos, lat, lon, delta, inicio, horas, paso_min)`: recibe el diccionario que devuelve `cargar_objetos` y cuenta cuántos satélites hay dentro del cuadro en cada instante. Devuelve una tupla de dos arrays de numpy `(minutos, cantidades)`: `minutos` tiene los minutos transcurridos desde `inicio` (`0, paso_min, 2 * paso_min, ...`) y `cantidades` la cantidad de satélites en el cuadro en cada uno de esos minutos. Usen `obtener_trayectoria` para cada satélite y operaciones de numpy sobre los arrays (comparaciones, `&`, `np.abs`) en lugar de recorrer los instantes uno por uno. Pista: sumar un array de `True`/`False` a un array de enteros suma 1 donde hay `True`.

### 4. Gráficos (módulo `graficos.py`)

Cada función recibe los datos y un nombre de archivo, guarda la figura en `salidas/` y también la muestra en el notebook. Todos los gráficos llevan título y etiquetas en los ejes.

- `barras_por_grupo(conteo, archivo)`: gráfico de barras con lo que devuelve `contar_por_grupo`.
- `barras_por_tipo(conteo, archivo)`: gráfico de barras con lo que devuelve `contar_por_tipo`.
- `histograma_altitudes(satelites, archivo)`: histograma con el eje X en escala logarítmica.
- `grafico_linea_de_tiempo(series, archivo)`: recibe un diccionario `{etiqueta: (anios, acumulado)}` y dibuja una línea por cada elemento, con leyenda. Así se pueden comparar, por ejemplo, el total, Starlink y el resto.
- `mapa(satelites, ciudad, lat, lon, delta, archivo="salidas/mapa_satelital.png")`:
  - eje X longitud (-180° a 180°), eje Y latitud (-90° a 90°);
  - todos los satélites como puntos pequeños;
  - la ciudad con una estrella;
  - en otro color, los satélites que caen dentro del cuadro (también dibujar el cuadro);
  - leyenda.
- `mapa_trayectoria(trayectoria, nombre, archivo)`: la traza de un satélite sobre el mapa.
- `linea_en_el_tiempo(minutos, cantidades, archivo)`: gráfico de línea con lo que devuelve `en_region_en_el_tiempo`, con el eje X en horas.
- `mapa_densidad(satelites, archivo)`: mapa de densidad que muestra cuántos satélites hay en cada celda de 5° × 5°. Usen `np.histogram2d` para contar y `plt.pcolormesh` (o `plt.imshow`) para dibujar, con una barra de colores (`plt.colorbar`).

### 5. El notebook (`informe.ipynb`)

Es el informe del trabajo. Tiene que contener celdas de texto (Markdown) que expliquen lo que se hace y lo que se ve, y celdas de código que sólo importen y llamen a funciones de los módulos.

Secciones mínimas:

1. Carga de datos: cuántos satélites tiene el archivo y cuántos descarta `crear_satelites`.
2. Grupos: conteo por grupo y gráfico de barras. ¿Qué porcentaje del total es Starlink?
3. Línea de tiempo: la cantidad acumulada de satélites de 1990 a 2026, con una línea para el total, otra para Starlink y otra para el resto. Una o dos oraciones que describan cómo cambió la cantidad y desde qué año. Tengan en cuenta que 2026 todavía no terminó.
4. Tipos de órbita: conteo y gráfico de barras.
5. Altitudes: histograma, y una o dos oraciones que describan en qué rangos de altitud se concentran los satélites.
6. Extremos: el más bajo, el más alto y el top 10 de cada uno (imprimir usando `__str__`).
7. Comparación de grupos: una tabla con el resumen de altitudes de cada grupo.
8. Bariloche: satélites en el cuadro con `lat = -41.13`, `lon = -71.30`, `delta = 5`, y el mapa.
9. Bariloche durante un día: con `en_region_en_el_tiempo`, cuántos satélites hay en el mismo cuadro cada 10 minutos durante 24 horas, el gráfico de línea, y el mínimo, el máximo y el promedio. Como referencia, la cantidad va de 28 a 70.
10. Densidad: el mapa de densidad en la fecha de referencia, y una o dos oraciones que describan en qué zonas hay más satélites.
11. La ISS: su trayectoria durante 3 horas (paso de 1 minuto), el mapa de la traza y sus pases sobre Bariloche en 24 h (con `delta = 10`), en hora argentina (UTC-3).
12. Conclusiones: un párrafo que resuma qué grupo predomina, desde qué año creció más rápido la cantidad de satélites, qué tipo de órbita predomina, cuántos satélites hay sobre Bariloche a lo largo del día y cuántas veces pasa la ISS por la zona.

---

## Reglas

- En el notebook no se definen funciones ni clases: todo lo reutilizable va en los módulos.
- El notebook tiene que correr de principio a fin sin errores con la opción Restart & Run All del menú Kernel, y se entrega con las salidas guardadas.
- Los módulos no imprimen ni grafican al importarse. Si quieren probar algo dentro de un módulo, usen `if __name__ == "__main__":`.
- Cada función y método lleva un *docstring*.
- El archivo provisto `tests.py` prueba las clases y funciones de los cuatro módulos. Se corre con `python tests.py` desde la carpeta del proyecto y muestra qué pruebas pasan y cuáles fallan. Úsenlo mientras programan: el trabajo tiene que pasar todas las pruebas. No lo modifiquen; si quieren agregar pruebas propias, háganlo en otro archivo (por ejemplo, `mis_tests.py`).

## Trabajo en grupo

- Repositorio único por grupo, con commits de los dos integrantes. Se revisa con `git log`.
- Una división posible: una persona hace `catalogo.py` y `satelite.py`, la otra `analisis.py` y `graficos.py`, y el notebook lo hacen entre las dos. Cada una revisa el código de la otra.
- El `README.md` incluye los integrantes, qué hizo cada uno y cómo correr el proyecto.

---

## Estructura del repositorio

```
proyecto-satelites/
├── README.md
├── .gitignore
├── funciones_base.py
├── catalogo.py
├── satelite.py
├── analisis.py
├── graficos.py
├── tests.py
├── informe.ipynb
├── datos/
│   └── satelites.json
└── salidas/
    ├── mapa_satelital.png
    └── ...
```
