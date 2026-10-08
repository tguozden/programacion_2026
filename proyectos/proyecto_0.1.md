# Extensión proyecto 0

El programa tendrá funcionalidades distintas dependiendo del archivo que se pase por parámetro. El archivo se pasará con su ruta, incluyendo la carpeta; por ejemplo:

```bash
python smn.py datos/estado_tiempo20261001.txt
python smn.py obs_json/estado_tiempo20261001.json
```

Los archivos `.txt` del SMN deberán estar en la carpeta `datos/`.

1. Si se pasa un archivo `.txt` del SMN:
    a. El programa detectará si el archivo está codificado en `latin-1` o en `utf-8` y lo leerá con la codificación correspondiente.
    b. Convertirá el diccionario de observaciones a formato `json`, con la fecha en formato ISO 8601 sin segundos (por ejemplo, `'2026-10-01T00:00'`). Como referencia, se puede obtener con `fecha.isoformat(timespec='minutes')`, donde `fecha` es el objeto `datetime.datetime` del diccionario.
    c. Luego guardará el objeto json, con codificación `utf-8`, en el directorio `obs_json/`, creando el directorio si no existe. El archivo tendrá el mismo nombre que el `.txt`, pero con extensión `.json` (por ejemplo, a `datos/estado_tiempo20261001.txt` le corresponde `obs_json/estado_tiempo20261001.json`).
    d. El programa imprimirá en stdout una leyenda antes de cada acción e indicará si se completó o no; por ejemplo: `'archivo del SMN, convirtiendo a json...'`, `'el directorio obs_json no existe, creándolo...'`, etc. Luego imprimirá, también en stdout y en a lo sumo 2 líneas, la cantidad de ciudades que contiene el archivo y la cantidad de ciudades informadas.
2. Si se pasa un archivo `.json` (siempre codificado en `utf-8`), imprimirá en stdout, en a lo sumo 2 líneas, la cantidad de ciudades que contiene el archivo y la cantidad de ciudades informadas.
3. Si no se pasa ningún archivo, dará aviso al usuario e informará además cuántos archivos `.txt` hay en `datos/` y cuántos `.json` hay en `obs_json/`.
4. Si se pasa más de un parámetro, dará aviso y terminará sin hacer nada más.
