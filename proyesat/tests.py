"""
tests.py
--------
Pruebas de la Etapa 1 con assert. Se corren desde esta carpeta con:

    python tests.py

(también funcionan con pytest, si está instalado).
"""

import json
import os
import tempfile
from datetime import datetime, timedelta, timezone

from catalogo import (GRUPOS, leer_satelites, anio_lanzamiento, grupo,
                      contar_por_grupo, lanzamientos_por_anio)
from satelite import Satelite, crear_satelites
from analisis import (contar_por_tipo, mas_bajo, mas_alto, en_zona,
                      ordenar_por, top_n, resumen_por_grupo)

BARILOCHE = (-76.30, -46.13, -66.30, -36.13)

# ---------------------------------------------------------------------------
# Datos de prueba
# ---------------------------------------------------------------------------

# Registros mínimos: sólo las claves que usa catalogo.py
REGISTROS = [
    {"OBJECT_NAME": "STARLINK-1007", "OBJECT_ID": "2019-074A"},
    {"OBJECT_NAME": "STARLINK-1008", "OBJECT_ID": "2019-074B"},
    {"OBJECT_NAME": "STARLINK-30000", "OBJECT_ID": "2023-010C"},
    {"OBJECT_NAME": "ONEWEB-0012", "OBJECT_ID": "2019-010A"},
    {"OBJECT_NAME": "NAVSTAR 80 (USA 309)", "OBJECT_ID": "2020-078A"},
    {"OBJECT_NAME": "ISS (ZARYA)", "OBJECT_ID": "1998-067A"},
    {"OBJECT_NAME": "CALSPHERE 1", "OBJECT_ID": "1964-063C"},
]

# Registro completo de la ISS, tal como viene en datos/satelites.json
ISS = {
    "OBJECT_NAME": "ISS (ZARYA)", "OBJECT_ID": "1998-067A",
    "EPOCH": "2026-10-27T04:14:31.558560", "MEAN_MOTION": 15.49073103,
    "ECCENTRICITY": 0.00069486, "INCLINATION": 51.6336, "RA_OF_ASC_NODE": 6.9404,
    "ARG_OF_PERICENTER": 314.9066, "MEAN_ANOMALY": 45.1358, "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U", "NORAD_CAT_ID": 25544, "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 59221, "BSTAR": 0.00011132043, "MEAN_MOTION_DOT": 5.704e-05,
    "MEAN_MOTION_DDOT": 0,
}

# Registro inventado de un satélite muy bajo y con mucho roce:
# 24 horas después del EPOCH el cálculo da unos 95 km de altitud
CAIDO = dict(ISS, OBJECT_NAME="CAIDO", MEAN_MOTION=16.4, BSTAR=0.001)

MOMENTO = datetime(2026, 10, 28, 4, 14, tzinfo=timezone.utc)   # EPOCH + 1 día


def satelites_de_prueba():
    """Devuelve una lista de objetos Satelite con altitudes y posiciones conocidas."""
    return [
        Satelite("STARLINK-1007", -41.0, -71.0, 550.0),     # LEO, en Bariloche
        Satelite("STARLINK-1008", 10.0, 20.0, 540.0),       # LEO
        Satelite("ISS (ZARYA)", -40.0, -70.0, 419.7),       # LEO, en Bariloche
        Satelite("NAVSTAR 80 (USA 309)", 30.0, -50.0, 20200.0),  # MEO
        Satelite("INTELSAT 901", 0.0, -18.0, 35786.0),      # GEO
        Satelite("TESS", -20.0, 100.0, 250000.0),           # HEO
    ]


# ---------------------------------------------------------------------------
# catalogo.py
# ---------------------------------------------------------------------------

def test_leer_satelites():
    """Lee un JSON temporal y devuelve la misma lista de registros."""
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = os.path.join(carpeta, "prueba.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(REGISTROS, f)
        registros = leer_satelites(ruta)
    assert isinstance(registros, list)
    assert registros == REGISTROS


def test_leer_satelites_inexistente():
    """Si el archivo no existe devuelve una lista vacía."""
    assert leer_satelites("no_existe_este_archivo.json") == []


def test_leer_satelites_archivo_provisto():
    """El archivo provisto tiene 16.822 registros, cada uno con nombre e identificador."""
    registros = leer_satelites("datos/satelites.json")
    assert len(registros) == 16822
    assert all("OBJECT_NAME" in r and "OBJECT_ID" in r for r in registros)


def test_anio_lanzamiento():
    """Toma los primeros cuatro caracteres de OBJECT_ID como int."""
    assert anio_lanzamiento({"OBJECT_ID": "1998-067A"}) == 1998
    assert anio_lanzamiento({"OBJECT_ID": "2023-010C"}) == 2023
    assert isinstance(anio_lanzamiento(ISS), int)


def test_grupo():
    """Cada prefijo de la tabla da su grupo; el resto da "Otros"."""
    assert grupo("STARLINK-1007") == "Starlink"
    assert grupo("ONEWEB-0012") == "OneWeb"
    assert grupo("KUIPER-00010") == "Kuiper"
    assert grupo("QIANFAN-1") == "Qianfan"
    assert grupo("IRIDIUM 106") == "Iridium"
    assert grupo("GLOBALSTAR M087") == "Globalstar"
    assert grupo("NAVSTAR 80 (USA 309)") == "GPS"
    assert grupo("BEIDOU-3 M1") == "BeiDou"
    assert grupo("ISS (ZARYA)") == "Otros"
    assert grupo("") == "Otros"


def test_grupo_solo_al_principio():
    """El prefijo tiene que estar al principio del nombre, no en cualquier lugar."""
    assert grupo("MI STARLINK") == "Otros"
    assert grupo("XNAVSTAR") == "Otros"


def test_tabla_grupos():
    """GRUPOS es un diccionario con los ocho prefijos de la tabla."""
    assert isinstance(GRUPOS, dict)
    assert len(GRUPOS) == 8
    assert GRUPOS["NAVSTAR"] == "GPS"


def test_contar_por_grupo():
    """Cuenta los satélites de cada grupo."""
    conteo = contar_por_grupo(REGISTROS)
    assert conteo["Starlink"] == 3
    assert conteo["OneWeb"] == 1
    assert conteo["GPS"] == 1
    assert conteo["Otros"] == 2
    assert sum(conteo.values()) == len(REGISTROS)
    assert contar_por_grupo([]) == {}


def test_lanzamientos_por_anio():
    """Cuenta los satélites lanzados cada año."""
    conteo = lanzamientos_por_anio(REGISTROS)
    assert conteo == {2019: 3, 2023: 1, 2020: 1, 1998: 1, 1964: 1}
    assert lanzamientos_por_anio([]) == {}


# ---------------------------------------------------------------------------
# satelite.py
# ---------------------------------------------------------------------------

def test_satelite_atributos():
    """El constructor guarda los cuatro datos como atributos."""
    sat = Satelite("ISS (ZARYA)", -41.0, -71.0, 419.73)
    assert sat.nombre == "ISS (ZARYA)"
    assert sat.latitud == -41.0
    assert sat.longitud == -71.0
    assert sat.altitud_km == 419.73


def test_tipo_orbita():
    """Clasificación por altitud, incluyendo los límites de la tabla."""
    assert Satelite("A", 0, 0, 100).tipo_orbita() == "LEO"
    assert Satelite("A", 0, 0, 1999.9).tipo_orbita() == "LEO"
    assert Satelite("A", 0, 0, 2000).tipo_orbita() == "MEO"
    assert Satelite("A", 0, 0, 20200).tipo_orbita() == "MEO"
    assert Satelite("A", 0, 0, 33999.9).tipo_orbita() == "MEO"
    assert Satelite("A", 0, 0, 34000).tipo_orbita() == "GEO"
    assert Satelite("A", 0, 0, 35786).tipo_orbita() == "GEO"
    assert Satelite("A", 0, 0, 37000).tipo_orbita() == "GEO"
    assert Satelite("A", 0, 0, 37000.1).tipo_orbita() == "HEO"
    assert Satelite("A", 0, 0, 250000).tipo_orbita() == "HEO"


def test_esta_en_zona():
    """Adentro, afuera y en el borde de la zona."""
    assert Satelite("A", -41.0, -71.0, 500).esta_en_zona(BARILOCHE)
    assert not Satelite("A", 41.0, -71.0, 500).esta_en_zona(BARILOCHE)    # latitud fuera
    assert not Satelite("A", -41.0, 71.0, 500).esta_en_zona(BARILOCHE)    # longitud fuera
    assert not Satelite("A", -41.0, -80.0, 500).esta_en_zona(BARILOCHE)
    assert not Satelite("A", -30.0, -71.0, 500).esta_en_zona(BARILOCHE)
    # el borde cuenta como adentro
    assert Satelite("A", -46.13, -76.30, 500).esta_en_zona(BARILOCHE)
    assert Satelite("A", -36.13, -66.30, 500).esta_en_zona(BARILOCHE)
    assert Satelite("A", -41.0, -66.30, 500).esta_en_zona(BARILOCHE)


def test_esta_en_zona_no_confunde_lat_lon():
    """La zona es (lon_min, lat_min, lon_max, lat_max): no hay que invertir el orden."""
    zona = (0, 50, 10, 60)          # longitudes 0 a 10, latitudes 50 a 60
    assert Satelite("A", 55, 5, 500).esta_en_zona(zona)
    assert not Satelite("A", 5, 55, 500).esta_en_zona(zona)


def test_str():
    """El formato es 'nombre | tipo | altitud con un decimal km'."""
    assert str(Satelite("ISS (ZARYA)", -41.0, -71.0, 419.73)) == "ISS (ZARYA) | LEO | 419.7 km"
    assert str(Satelite("INTELSAT 901", 0, -18, 35786)) == "INTELSAT 901 | GEO | 35786.0 km"
    assert str(Satelite("X", 0, 0, 20200.06)) == "X | MEO | 20200.1 km"


def test_crear_satelites():
    """Calcula la posición de la ISS: un Satelite con valores razonables."""
    satelites = crear_satelites([ISS], MOMENTO)
    assert len(satelites) == 1
    iss = satelites[0]
    assert isinstance(iss, Satelite)
    assert iss.nombre == "ISS (ZARYA)"
    assert -90 <= iss.latitud <= 90
    assert -180 <= iss.longitud <= 180
    assert 380 < iss.altitud_km < 450
    assert iss.tipo_orbita() == "LEO"


def test_crear_satelites_descarta_caidos():
    """Descarta el satélite cuya altitud da menor a 100 km y conserva el resto."""
    satelites = crear_satelites([ISS, CAIDO, ISS], MOMENTO)
    nombres = [s.nombre for s in satelites]
    assert nombres == ["ISS (ZARYA)", "ISS (ZARYA)"]
    assert crear_satelites([CAIDO], MOMENTO) == []
    assert crear_satelites([], MOMENTO) == []


def test_crear_satelites_momento_sin_zona_horaria():
    """Un datetime sin zona horaria se toma como UTC (lo resuelve obtener_posicion)."""
    con_tz = crear_satelites([ISS], MOMENTO)[0]
    sin_tz = crear_satelites([ISS], MOMENTO.replace(tzinfo=None))[0]
    assert con_tz.altitud_km == sin_tz.altitud_km
    assert con_tz.latitud == sin_tz.latitud


def test_crear_satelites_lejos_del_epoch():
    """A una hora del EPOCH la ISS se movió, pero sigue en órbita baja."""
    antes = crear_satelites([ISS], MOMENTO)[0]
    despues = crear_satelites([ISS], MOMENTO + timedelta(hours=1))[0]
    assert (antes.latitud, antes.longitud) != (despues.latitud, despues.longitud)
    assert despues.tipo_orbita() == "LEO"


# ---------------------------------------------------------------------------
# analisis.py
# ---------------------------------------------------------------------------

def test_contar_por_tipo():
    """Cuenta por tipo de órbita, con las cuatro claves siempre presentes."""
    assert contar_por_tipo(satelites_de_prueba()) == {"LEO": 3, "MEO": 1, "GEO": 1, "HEO": 1}
    assert contar_por_tipo([]) == {"LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}
    solo_leo = [Satelite("A", 0, 0, 500), Satelite("B", 0, 0, 600)]
    assert contar_por_tipo(solo_leo) == {"LEO": 2, "MEO": 0, "GEO": 0, "HEO": 0}


def test_mas_bajo_y_mas_alto():
    """Devuelven el objeto Satelite (no la altitud) de menor y mayor altitud."""
    satelites = satelites_de_prueba()
    bajo = mas_bajo(satelites)
    alto = mas_alto(satelites)
    assert isinstance(bajo, Satelite)
    assert bajo.nombre == "ISS (ZARYA)"
    assert alto.nombre == "TESS"
    uno = [Satelite("UNICO", 0, 0, 1000)]
    assert mas_bajo(uno) is uno[0]
    assert mas_alto(uno) is uno[0]


def test_en_zona():
    """Devuelve una lista con los satélites dentro de la zona."""
    adentro = en_zona(satelites_de_prueba(), BARILOCHE)
    assert isinstance(adentro, list)
    assert sorted(s.nombre for s in adentro) == ["ISS (ZARYA)", "STARLINK-1007"]
    assert en_zona([], BARILOCHE) == []
    assert en_zona(satelites_de_prueba(), (0, 80, 1, 81)) == []


def test_ordenar_por():
    """Ordena por cualquier atributo, ascendente o descendente."""
    satelites = satelites_de_prueba()
    por_altitud = ordenar_por(satelites, "altitud_km")
    assert [s.altitud_km for s in por_altitud] == [419.7, 540.0, 550.0, 20200.0, 35786.0, 250000.0]
    por_altitud_desc = ordenar_por(satelites, "altitud_km", descendente=True)
    assert [s.altitud_km for s in por_altitud_desc] == [250000.0, 35786.0, 20200.0, 550.0, 540.0, 419.7]
    por_nombre = ordenar_por(satelites, "nombre")
    assert [s.nombre for s in por_nombre] == sorted(s.nombre for s in satelites)
    por_latitud = ordenar_por(satelites, "latitud")
    assert [s.latitud for s in por_latitud] == [-41.0, -40.0, -20.0, 0.0, 10.0, 30.0]


def test_ordenar_por_no_modifica_la_original():
    """Devuelve una lista nueva y deja la original como estaba."""
    satelites = satelites_de_prueba()
    nombres_antes = [s.nombre for s in satelites]
    ordenados = ordenar_por(satelites, "altitud_km")
    assert ordenados is not satelites
    assert [s.nombre for s in satelites] == nombres_antes


def test_top_n():
    """Los n más altos o más bajos."""
    satelites = satelites_de_prueba()
    assert [s.nombre for s in top_n(satelites, 2)] == ["TESS", "INTELSAT 901"]
    assert [s.nombre for s in top_n(satelites, 2, mas_altos=False)] == ["ISS (ZARYA)", "STARLINK-1008"]
    assert top_n(satelites, 0) == []
    assert len(top_n(satelites, 100)) == len(satelites)


def test_resumen_por_grupo():
    """Cantidad, mínima, media y máxima de las altitudes de cada grupo, sin redondear."""
    resumen = resumen_por_grupo(satelites_de_prueba())
    assert set(resumen) == {"Starlink", "GPS", "Otros"}
    assert resumen["Starlink"] == {"cantidad": 2, "minima": 540.0, "media": 545.0, "maxima": 550.0}
    assert resumen["GPS"] == {"cantidad": 1, "minima": 20200.0, "media": 20200.0, "maxima": 20200.0}
    otros = resumen["Otros"]
    assert otros["cantidad"] == 3
    assert otros["minima"] == 419.7
    assert otros["maxima"] == 250000.0
    assert abs(otros["media"] - (419.7 + 35786.0 + 250000.0) / 3) < 1e-9
    assert resumen_por_grupo([]) == {}


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    pruebas = [f for nombre, f in list(globals().items())
               if nombre.startswith("test_") and callable(f)]
    fallas = 0
    for prueba in pruebas:
        try:
            prueba()
            print("ok   ", prueba.__name__)
        except Exception as e:
            fallas += 1
            print("FALLA", prueba.__name__, "->", type(e).__name__, e)
    print(f"\n{len(pruebas) - fallas} de {len(pruebas)} pruebas pasaron")
