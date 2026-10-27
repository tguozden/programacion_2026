def buscar(nombre):
    try:
        import funciones_smn
    except ImportError:
        raise ImportError(f"no encontré la función {nombre} (y no hay funciones_smn.py)")
    if nombre in vars(funciones_smn):
        return vars(funciones_smn)[nombre]

    raise ImportError(f"no encontré la función {nombre}")


def test_leer_observaciones_basico():
    func = buscar('leer_observaciones')
    obs = func("archivos_de_prueba/basico.txt")
    assert "Azul" in obs
    assert obs["Azul"]["temperatura"] == 3.3
    assert obs["Azul"]["direccion_viento"] == "Sur", 'dirección de viento'
    assert obs["Azul"]["velocidad_viento"] == 5


def test_leer_observaciones_limpia_nombre_ciudad():
    func = buscar('leer_observaciones')
    obs = func("archivos_de_prueba/con_espacios.txt")
    assert "La Plata" in obs, f'ciudades: {list(obs)}'


def test_leer_observaciones_calma():
    func = buscar('leer_observaciones')
    obs = func("archivos_de_prueba/con_faltantes.txt")
    assert obs["Rosario"]["direccion_viento"] == "Calma"
    assert obs["Rosario"]["velocidad_viento"] in (0, None), 'velocidad con Calma'


def test_leer_observaciones_malformado():
    func = buscar('leer_observaciones')
    obs = func("archivos_de_prueba/malformado.txt")
    assert len(obs) == 2, f'{len(obs)} ciudades'
    assert "LineaRota" not in obs


def test_leer_observaciones_vacio():
    func = buscar('leer_observaciones')
    obs = func("archivos_de_prueba/vacio.txt")
    assert len(obs) == 0


def test_leer_observaciones_smn():
    func = buscar('leer_observaciones')
    obs = func("archivos_de_prueba/estado_tiempo20260922.txt")
    assert len(obs) == 121, f'{len(obs)} ciudades'
    assert "Bahía Blanca" in obs, 'encoding'


def test_parsear_fecha_hora():
    func = buscar('parsear_fecha_hora')
    fecha = func("10-septiembre-2026", "08:00")
    assert fecha.month == 9
    fecha = func("10-julio-2000", "16:00")
    assert fecha.month == 7
    assert fecha.hour == 16


def test_separar_viento():
    func = buscar('separar_viento')
    assert func("Norte  3") == ("Norte", 3)
    assert func("Sudoeste  33") == ("Sudoeste", 33)
    assert func("Calma")[0] == "Calma"


def test_cantidad_ciudades():
    leer = buscar('leer_observaciones')
    func = buscar('cantidad_ciudades')
    cantidad = func(leer("archivos_de_prueba/basico.txt"))
    assert cantidad == 2, f'basico: {cantidad}'
    cantidad = func(leer("archivos_de_prueba/estado_tiempo20260922.txt"))
    assert cantidad == 121, f'smn: {cantidad}'


def test_cantidad_ciudades_completas():
    leer = buscar('leer_observaciones')
    func = buscar('cantidad_ciudades_completas')
    completas = func(leer("archivos_de_prueba/basico.txt"))
    assert completas == 2, f'basico: {completas}'
    completas = func(leer("archivos_de_prueba/con_faltantes.txt"))
    assert completas == 0, f'con_faltantes: {completas}'
    # Junín está en Calma, y eso no es un dato faltante
    completas = func(leer("archivos_de_prueba/horarios.txt"))
    assert completas == 3, f'horarios: {completas}, ¿Calma cuenta como faltante?'
    completas = func(leer("archivos_de_prueba/estado_tiempo20260922.txt"))
    assert completas == 62, f'smn: {completas}'


def test_top_n_ciudades():
    leer = buscar('leer_observaciones')
    func = buscar('top_n_ciudades')
    obs = leer("archivos_de_prueba/basico.txt")
    top = func(obs, "temperatura", 1, descendente=True)
    assert len(top) == 1 and "Azul" in top[0], f'más cálida: {top}'
    top = func(obs, "velocidad_viento", 2, descendente=False)
    assert "Azul" in top[0] and "Bahía Blanca" in top[1], f'menos viento: {top}'


def test_horarios_reportados():
    leer = buscar('leer_observaciones')
    func = buscar('horarios_reportados')
    horarios = func(leer("archivos_de_prueba/horarios.txt"))
    assert horarios == ["08:00", "21:00"], f'horarios: {horarios}'


def main():
    funciones = [func for nombre, func in globals().items() if nombre.startswith('test_')]
    for func in funciones:
        try:
            func()
            print(func.__name__, '\t\tok')
        except AssertionError as e:
            print('falló', func.__name__, 'assert: ', e)
        except Exception as e:
            print('error', func.__name__, 'inesperado: ', type(e).__name__, e)


if __name__ == "__main__":
    main()
