import analisis_smn

def buscar(nombre):
    if nombre in vars(analisis_smn):
        return vars(analisis_smn)[nombre]

    import funciones_smn
    if nombre in vars(funciones_smn):
        return vars(funciones_smn)[nombre]

    raise ImportError(f"no encontré la función {nombre}")


def test_leer_observaciones_basico():
    func = buscar('leer_observaciones')
    obs = func("tests/basico.txt")
    assert "Azul" in obs
    assert obs["Azul"]["temperatura"] == 3.3
    assert obs["Azul"]["direccion_viento"] == "Sur", 'dirección de viento'
    assert obs["Azul"]["velocidad_viento"] == 5


def test_parsear_fecha_hora():
    func = buscar('parsear_fecha_hora')
    fecha = func("10-septiembre-2026", "08:00")
    assert fecha.month == 9
    fecha = func("10-julio-2000", "16:00")
    assert fecha.month == 8
    assert fecha.hour == 16



def main():
    funciones = [test_leer_observaciones_basico, test_parsear_fecha_hora]
    for func in funciones:
        try:
            func()
        except Exception as e:
            print('falló', func.__name__, 'error: ', type(e).__name__, e)
        else:
            print(func.__name__, '\t\tok')
    
    
        

if __name__ == "__main__":
    main()
