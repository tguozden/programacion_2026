"""
tests.py
--------
Pruebas provistas. Se corren con:

    python tests.py

No modificar este archivo. Algunas pruebas usan datos/satelites.json y FECHA_REF,
así que no reemplacen ese archivo.
"""

import json
import os
from datetime import datetime, timedelta, timezone

import numpy as np
import matplotlib
matplotlib.use("Agg")  # los gráficos se guardan pero no se muestran
import matplotlib.pyplot as plt
plt.show = lambda *args, **kwargs: None

FECHA_REF = datetime(2026, 10, 19, 12, 0, tzinfo=timezone.utc)
ARCHIVO = "datos/satelites.json"
BARILOCHE = (-41.13, -71.30)

ISS = {
    "OBJECT_NAME": "ISS (ZARYA)", "OBJECT_ID": "1998-067A", "EPOCH": "2026-10-14T08:06:39.057984",
    "MEAN_MOTION": 15.48861773, "ECCENTRICITY": 0.00067245, "INCLINATION": 51.6325,
    "RA_OF_ASC_NODE": 70.4557, "ARG_OF_PERICENTER": 261.592, "MEAN_ANOMALY": 98.4307,
    "EPHEMERIS_TYPE": 0, "CLASSIFICATION_TYPE": "U", "NORAD_CAT_ID": 25544, "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 59022, "BSTAR": 0.00011949953, "MEAN_MOTION_DOT": 6.109e-05, "MEAN_MOTION_DDOT": 0,
}
ISS_POSICION = (2.1503, -161.3743, 419.72)  # latitud, longitud y altitud en FECHA_REF


def ejemplos():
    """Lista chica de satélites armados a mano."""
    from satelite import Satelite
    return [
        Satelite("BAJO", 10.0, 20.0, 300.0),
        Satelite("MEDIO", -5.0, 100.0, 20200.0),
        Satelite("GEO-1", 0.1, -75.0, 35786.0),
        Satelite("LEJANO", 30.0, 0.0, 40000.0),
        Satelite("ALTO-LEO", -41.0, -71.0, 1200.0),
    ]


def registros_de_prueba():
    """Registros armados a mano, sólo con las claves que hacen falta."""
    return [
        {"OBJECT_NAME": "STARLINK-1007", "OBJECT_ID": "2019-074A"},
        {"OBJECT_NAME": "ISS (ZARYA)", "OBJECT_ID": "1998-067A"},
        {"OBJECT_NAME": "STARLINK-30000", "OBJECT_ID": "2021-005B"},
        {"OBJECT_NAME": "NAVSTAR 43 (USA 132)", "OBJECT_ID": "1997-035A"},
        {"OBJECT_NAME": "STARLINK-31000", "OBJECT_ID": "2021-040C"},
    ]


def iss():
    """Objeto de Skyfield de la ISS (sin usar catalogo.py)."""
    from funciones_base import crear_objeto_skyfield
    return crear_objeto_skyfield(ISS)


def cerca(a, b, tolerancia=0.01):
    return abs(a - b) <= tolerancia


# ---------- catalogo.py ----------

def test_leer_satelites():
    from catalogo import leer_satelites
    registros = leer_satelites(ARCHIVO)
    assert isinstance(registros, list)
    assert len(registros) == 16710
    assert registros[0]["OBJECT_NAME"] == "CALSPHERE 1"
    assert ISS in registros


def test_leer_satelites_inexistente():
    from catalogo import leer_satelites
    assert leer_satelites("datos/no_existe.json") == []


def test_anio_lanzamiento():
    from catalogo import anio_lanzamiento
    assert anio_lanzamiento(ISS) == 1998
    assert anio_lanzamiento({"OBJECT_NAME": "X", "OBJECT_ID": "2026-001A"}) == 2026


def test_grupo():
    from catalogo import grupo
    assert grupo("STARLINK-1007") == "Starlink"
    assert grupo("ONEWEB-0012") == "OneWeb"
    assert grupo("KUIPER-00010") == "Kuiper"
    assert grupo("QIANFAN-1") == "Qianfan"
    assert grupo("IRIDIUM 106") == "Iridium"
    assert grupo("GLOBALSTAR M073") == "Globalstar"
    assert grupo("NAVSTAR 43 (USA 132)") == "GPS"
    assert grupo("BEIDOU-3 M1") == "BeiDou"
    assert grupo("ISS (ZARYA)") == "Otros"
    assert grupo("XSTARLINK") == "Otros", "el nombre tiene que empezar con el prefijo"


def test_contar_por_grupo():
    from catalogo import contar_por_grupo
    conteo = contar_por_grupo(registros_de_prueba())
    assert conteo == {"Starlink": 3, "Otros": 1, "GPS": 1}
    assert list(conteo)[0] == "Starlink", "ordenado de mayor a menor cantidad"
    assert contar_por_grupo([]) == {}


def test_filtrar_por_grupo():
    from catalogo import filtrar_por_grupo
    starlink = filtrar_por_grupo(registros_de_prueba(), "Starlink")
    assert [r["OBJECT_NAME"] for r in starlink] == ["STARLINK-1007", "STARLINK-30000", "STARLINK-31000"]
    assert filtrar_por_grupo(registros_de_prueba(), "Kuiper") == []


def test_lanzamientos_por_anio():
    from catalogo import lanzamientos_por_anio
    conteo = lanzamientos_por_anio(registros_de_prueba())
    assert conteo == {1997: 1, 1998: 1, 2019: 1, 2021: 2}
    assert list(conteo) == [1997, 1998, 2019, 2021], "las claves van ordenadas por año"
    assert lanzamientos_por_anio([]) == {}


def test_linea_de_tiempo():
    from catalogo import linea_de_tiempo
    anios, acumulado = linea_de_tiempo(registros_de_prueba(), 1995, 2022)
    assert isinstance(anios, np.ndarray) and isinstance(acumulado, np.ndarray)
    assert list(anios) == list(range(1995, 2023)), "un elemento por año, incluidos los dos extremos"
    assert len(acumulado) == 28
    assert acumulado[0] == 0          # 1995
    assert acumulado[2] == 1          # 1997
    assert acumulado[3] == 2          # 1998
    assert acumulado[23] == 2         # 2018: los años sin lanzamientos repiten el valor anterior
    assert acumulado[24] == 3         # 2019
    assert acumulado[-1] == 5         # 2022


def test_cargar_objetos():
    from catalogo import cargar_objetos
    from funciones_base import obtener_posicion
    objetos = cargar_objetos([ISS])
    assert isinstance(objetos, dict)
    assert list(objetos) == ["ISS (ZARYA)"]
    lat, lon, alt = obtener_posicion(objetos["ISS (ZARYA)"], FECHA_REF)
    assert cerca(lat, ISS_POSICION[0]) and cerca(lon, ISS_POSICION[1]) and cerca(alt, ISS_POSICION[2])


# ---------- satelite.py ----------

def test_atributos():
    from satelite import Satelite
    s = Satelite("PRUEBA", -41.1, -71.3, 500.0)
    assert s.nombre == "PRUEBA"
    assert s.latitud == -41.1
    assert s.longitud == -71.3
    assert s.altitud_km == 500.0


def test_tipo_orbita():
    from satelite import Satelite
    assert Satelite("A", 0, 0, 500).tipo_orbita() == "LEO"
    assert Satelite("B", 0, 0, 1999.9).tipo_orbita() == "LEO"
    assert Satelite("C", 0, 0, 2000).tipo_orbita() == "MEO", "2000 km es MEO"
    assert Satelite("D", 0, 0, 20200).tipo_orbita() == "MEO"
    assert Satelite("E", 0, 0, 34000).tipo_orbita() == "GEO", "34000 km es GEO"
    assert Satelite("F", 0, 0, 35786).tipo_orbita() == "GEO"
    assert Satelite("G", 0, 0, 37000).tipo_orbita() == "GEO", "37000 km es GEO"
    assert Satelite("H", 0, 0, 37000.1).tipo_orbita() == "HEO"


def test_esta_en_region():
    from satelite import Satelite
    s = Satelite("PRUEBA", 10, 20, 500)
    assert s.esta_en_region(10, 20, 1)
    assert s.esta_en_region(9, 21, 1), "el borde del cuadro cuenta como adentro"
    assert not s.esta_en_region(8, 20, 1)
    assert not s.esta_en_region(10, 22, 1)
    assert not s.esta_en_region(-10, -20, 1)


def test_str():
    from satelite import Satelite
    assert str(Satelite("PRUEBA", 0, 0, 500)) == "PRUEBA | LEO | 500.0 km"
    assert str(Satelite("ISS (ZARYA)", 2.2, -161.3, 419.72)) == "ISS (ZARYA) | LEO | 419.7 km"


def test_crear_satelites():
    from satelite import Satelite, crear_satelites
    sats = crear_satelites([ISS], FECHA_REF)
    assert isinstance(sats, list)
    assert len(sats) == 1
    assert isinstance(sats[0], Satelite)
    assert sats[0].nombre == "ISS (ZARYA)"
    assert cerca(sats[0].latitud, ISS_POSICION[0])
    assert cerca(sats[0].longitud, ISS_POSICION[1])
    assert cerca(sats[0].altitud_km, ISS_POSICION[2])


def test_crear_satelites_descarta_bajos():
    from satelite import crear_satelites
    with open(ARCHIVO, encoding="utf-8") as f:
        registros = json.load(f)
    reingresados = [r for r in registros if r["OBJECT_NAME"] in ("BANDWAGON-2 OBJECT AE", "2023-091AS")]
    assert len(reingresados) == 2
    assert crear_satelites(reingresados + [ISS], FECHA_REF)[0].nombre == "ISS (ZARYA)"
    assert len(crear_satelites(reingresados, FECHA_REF)) == 0, "altitud menor a 100 km"


# ---------- analisis.py ----------

def test_contar_por_tipo():
    from analisis import contar_por_tipo
    assert contar_por_tipo(ejemplos()) == {"LEO": 2, "MEO": 1, "GEO": 1, "HEO": 1}
    assert contar_por_tipo(ejemplos()[:1]) == {"LEO": 1, "MEO": 0, "GEO": 0, "HEO": 0}


def test_mas_bajo_y_mas_alto():
    from analisis import mas_bajo, mas_alto
    assert mas_bajo(ejemplos()).nombre == "BAJO"
    assert mas_alto(ejemplos()).nombre == "LEJANO"


def test_en_region():
    from analisis import en_region
    lat, lon = BARILOCHE
    nombres = [s.nombre for s in en_region(ejemplos(), lat, lon, 1)]
    assert nombres == ["ALTO-LEO"]
    assert en_region(ejemplos(), 89, 179, 0.5) == []


def test_ordenar_por():
    from analisis import ordenar_por
    sats = ejemplos()
    copia = list(sats)
    por_altura = [s.nombre for s in ordenar_por(sats, "altitud_km")]
    assert por_altura == ["BAJO", "ALTO-LEO", "MEDIO", "GEO-1", "LEJANO"]
    por_nombre = [s.nombre for s in ordenar_por(sats, "nombre", descendente=True)]
    assert por_nombre == ["MEDIO", "LEJANO", "GEO-1", "BAJO", "ALTO-LEO"]
    por_latitud = [s.nombre for s in ordenar_por(sats, "latitud")]
    assert por_latitud == ["ALTO-LEO", "MEDIO", "GEO-1", "BAJO", "LEJANO"]
    assert sats == copia, "ordenar_por no debe modificar la lista original"


def test_top_n():
    from analisis import top_n
    assert [s.nombre for s in top_n(ejemplos(), 2)] == ["LEJANO", "GEO-1"]
    assert [s.nombre for s in top_n(ejemplos(), 3, mas_altos=False)] == ["BAJO", "ALTO-LEO", "MEDIO"]


def test_a_diccionario():
    from analisis import a_diccionario
    d = a_diccionario(ejemplos())
    assert isinstance(d, dict)
    assert len(d) == 5
    assert d["BAJO"] == {"latitud": 10.0, "longitud": 20.0, "altitud_km": 300.0, "tipo_orbita": "LEO"}
    assert d["LEJANO"]["tipo_orbita"] == "HEO"


def test_resumen_por_grupo():
    from analisis import resumen_por_grupo
    from satelite import Satelite
    sats = [
        Satelite("STARLINK-1", 0, 0, 500.0),
        Satelite("STARLINK-2", 0, 0, 600.0),
        Satelite("STARLINK-3", 0, 0, 550.0),
        Satelite("ISS (ZARYA)", 0, 0, 420.0),
    ]
    resumen = resumen_por_grupo(sats)
    assert set(resumen) == {"Starlink", "Otros"}
    assert resumen["Starlink"] == {"cantidad": 3, "minima": 500.0, "media": 550.0, "maxima": 600.0}
    assert resumen["Otros"] == {"cantidad": 1, "minima": 420.0, "media": 420.0, "maxima": 420.0}


def test_trayectoria():
    from analisis import trayectoria
    tray = trayectoria(iss(), FECHA_REF, 3, 1)
    assert len(tray) == 180
    assert tray[0][0] == FECHA_REF
    assert tray[1][0] == FECHA_REF + timedelta(minutes=1)
    momento, lat, lon, alt = tray[0]
    assert cerca(lat, ISS_POSICION[0]) and cerca(lon, ISS_POSICION[1]) and cerca(alt, ISS_POSICION[2])
    assert all(400 < p[3] < 440 for p in tray), "la ISS está siempre entre 400 y 440 km"
    assert len(trayectoria(iss(), FECHA_REF, 2, 10)) == 12


def test_pases_sobre():
    from analisis import pases_sobre
    lat, lon = BARILOCHE
    pases = pases_sobre(iss(), lat, lon, 10, FECHA_REF, 24)
    assert len(pases) == 5
    entrada, salida = pases[1]
    assert entrada.strftime("%H:%M") == "20:43"
    assert salida.strftime("%H:%M") == "20:47"
    entrada, salida = pases[0]
    assert entrada == salida, "un pase de un solo minuto entra y sale en el mismo minuto"
    assert pases_sobre(iss(), lat, lon, 10, FECHA_REF, 1) == []


def test_en_region_en_el_tiempo():
    from analisis import en_region_en_el_tiempo
    from funciones_base import crear_objeto_skyfield
    with open(ARCHIVO, encoding="utf-8") as f:
        registros = json.load(f)
    gps = {r["OBJECT_NAME"]: crear_objeto_skyfield(r) for r in registros if r["OBJECT_NAME"].startswith("NAVSTAR")}
    assert len(gps) == 40
    lat, lon = BARILOCHE
    minutos, cantidades = en_region_en_el_tiempo(gps, lat, lon, 20, FECHA_REF, 24, 10)
    assert isinstance(minutos, np.ndarray) and isinstance(cantidades, np.ndarray)
    assert len(minutos) == 144 and len(cantidades) == 144
    assert minutos[0] == 0 and minutos[1] == 10 and minutos[-1] == 1430
    assert list(cantidades[:6]) == [1, 2, 2, 2, 1, 1]
    assert cantidades.sum() == 228
    assert cantidades.max() == 4


# ---------- graficos.py ----------

def generar(funcion, *args):
    """Llama a una función de gráficos y verifica que haya creado el archivo."""
    os.makedirs("salidas", exist_ok=True)
    archivo = f"salidas/prueba_{funcion.__name__}.png"
    if os.path.exists(archivo):
        os.remove(archivo)
    funcion(*args, archivo)
    plt.close("all")
    assert os.path.exists(archivo), f"no se creó {archivo}"
    os.remove(archivo)


def test_mapa():
    from graficos import mapa
    lat, lon = BARILOCHE
    generar(mapa, ejemplos(), "Bariloche", lat, lon, 5)


def test_barras_por_tipo():
    from graficos import barras_por_tipo
    generar(barras_por_tipo, {"LEO": 2, "MEO": 1, "GEO": 1, "HEO": 1})


def test_barras_por_grupo():
    from graficos import barras_por_grupo
    generar(barras_por_grupo, {"Starlink": 3, "Otros": 1, "GPS": 1})


def test_histograma_altitudes():
    from graficos import histograma_altitudes
    generar(histograma_altitudes, ejemplos())


def test_mapa_trayectoria():
    from graficos import mapa_trayectoria
    from analisis import trayectoria
    generar(mapa_trayectoria, trayectoria(iss(), FECHA_REF, 3, 1), "ISS (ZARYA)")


def test_grafico_linea_de_tiempo():
    from graficos import grafico_linea_de_tiempo
    anios = np.arange(2000, 2011)
    series = {"Total": (anios, np.arange(11) * 2), "Starlink": (anios, np.arange(11))}
    generar(grafico_linea_de_tiempo, series)


def test_linea_en_el_tiempo():
    from graficos import linea_en_el_tiempo
    generar(linea_en_el_tiempo, np.arange(0, 1440, 10), np.arange(144) % 7)


def test_mapa_densidad():
    from graficos import mapa_densidad
    generar(mapa_densidad, ejemplos())


def main():
    funciones = [
        test_leer_satelites, test_leer_satelites_inexistente, test_anio_lanzamiento, test_grupo,
        test_contar_por_grupo, test_filtrar_por_grupo, test_lanzamientos_por_anio,
        test_linea_de_tiempo, test_cargar_objetos,
        test_atributos, test_tipo_orbita, test_esta_en_region, test_str,
        test_crear_satelites, test_crear_satelites_descarta_bajos,
        test_contar_por_tipo, test_mas_bajo_y_mas_alto, test_en_region, test_ordenar_por,
        test_top_n, test_a_diccionario, test_resumen_por_grupo,
        test_trayectoria, test_pases_sobre, test_en_region_en_el_tiempo,
        test_mapa, test_barras_por_tipo, test_barras_por_grupo, test_histograma_altitudes,
        test_mapa_trayectoria, test_grafico_linea_de_tiempo, test_linea_en_el_tiempo,
        test_mapa_densidad,
    ]
    pasaron = 0
    for func in funciones:
        try:
            func()
        except Exception as e:
            print('falló', func.__name__, 'error: ', type(e).__name__, e)
        else:
            print('pasó ', func.__name__)
            pasaron += 1
    print(f'\n{pasaron} de {len(funciones)} pruebas pasaron')


if __name__ == "__main__":
    main()
