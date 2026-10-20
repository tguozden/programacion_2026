"""
funciones_base.py
-----------------
Módulo provisto para el cálculo de posiciones satelitales
utilizando la librería Skyfield. No hace falta modificarlo.
"""

from datetime import datetime, timezone
import numpy as np
from skyfield.api import load, wgs84, EarthSatellite

# La escala de tiempo se crea una sola vez: crearla en cada llamada
# hace que calcular miles de posiciones sea ~30 veces más lento.
ts = load.timescale()

# Por el mismo motivo, los instantes de cada trayectoria se calculan una sola vez
_tiempos = {}


def crear_objeto_skyfield(registro: dict) -> EarthSatellite:
    """
    Crea el objeto satélite de Skyfield a partir de un registro (diccionario)
    leído de datos/satelites.json, tal como viene en el archivo.
    Este objeto es el que reciben obtener_posicion y obtener_trayectoria.
    """
    satelite = EarthSatellite.from_omm(ts, registro)
    satelite.name = registro["OBJECT_NAME"]
    return satelite


def obtener_posicion(satelite: EarthSatellite, momento: datetime) -> tuple:
    """
    Dado un objeto satélite de Skyfield y un datetime de Python (con o sin timezone),
    calcula y devuelve una tupla con (latitud, longitud, altitud_km).
    Si el datetime no tiene zona horaria, se asume UTC.

    - latitud: float entre -90.0 y 90.0
    - longitud: float entre -180.0 y 180.0
    - altitud_km: float (altura en kilómetros sobre la superficie)
    """
    # Asegurar que el datetime tenga zona horaria UTC para Skyfield
    if momento.tzinfo is None:
        momento = momento.replace(tzinfo=timezone.utc)

    t = ts.from_datetime(momento)
    geocentrico = satelite.at(t)
    subpoint = wgs84.subpoint(geocentrico)

    lat = subpoint.latitude.degrees
    lon = subpoint.longitude.degrees
    alt = subpoint.elevation.km

    return (round(float(lat), 4), round(float(lon), 4), round(float(alt), 3))


def obtener_trayectoria(satelite: EarthSatellite, inicio: datetime, horas: int, paso_min: int) -> tuple:
    """
    Calcula de una sola vez las posiciones de un satélite cada `paso_min` minutos
    durante `horas` horas, empezando en `inicio` (si no tiene zona horaria, se asume UTC).
    Devuelve una tupla de tres arrays de numpy, todos de largo horas * 60 // paso_min:
    (latitudes, longitudes, altitudes_km).

    Es mucho más rápida que llamar a obtener_posicion en un ciclo.
    """
    if inicio.tzinfo is None:
        inicio = inicio.replace(tzinfo=timezone.utc)
    inicio = inicio.astimezone(timezone.utc)

    clave = (inicio, horas, paso_min)
    if clave not in _tiempos:
        minutos = np.arange(horas * 60 // paso_min) * paso_min
        _tiempos[clave] = ts.utc(inicio.year, inicio.month, inicio.day, inicio.hour,
                                 inicio.minute + minutos, inicio.second)
    subpoint = wgs84.subpoint(satelite.at(_tiempos[clave]))

    return (subpoint.latitude.degrees, subpoint.longitude.degrees, subpoint.elevation.km)


def epoch_medio(registros: list) -> datetime:
    """
    Recibe la lista de registros leída de datos/satelites.json y devuelve
    la fecha media de sus "EPOCH" como datetime en UTC.
    Sirve para elegir un instante de cálculo cercano a los datos.
    """
    segundos = [datetime.fromisoformat(r["EPOCH"]).replace(tzinfo=timezone.utc).timestamp()
                for r in registros]
    return datetime.fromtimestamp(sum(segundos) / len(segundos), tz=timezone.utc)
