# Ejercicios – Módulo JSON

## Ejercicio 1: De diccionario a JSON

Dado el siguiente diccionario:

```python
alumno = {
    "nombre": "Marcos",
    "legajo": 4521,
    "activo": True,
    "materias_aprobadas": ["Álgebra", "Programación 1"],
    "promedio": None
}
```

- Convertirlo a JSON usando `json.dumps()` e imprimirlo.
- Volver a convertirlo, esta vez con `indent=4`, y comparar la legibilidad.
- Indicar qué tipo de dato tiene el resultado de `json.dumps()` (comprobarlo con `type()`).

## Ejercicio 2: Guardar y volver a leer

A partir del diccionario `alumno` del ejercicio anterior:

- Guardarlo en un archivo `alumno.json` con `json.dump()`.
- Abrir el archivo en un editor de texto y revisar cómo quedó escrito `None` y `True`.
- Cargarlo de nuevo en una variable nueva llamada `alumno_cargado` con `json.load()` y verificar con `==` que sea igual al diccionario original.

## Ejercicio 3: Encontrar el error

El siguiente texto quiere ser un archivo JSON válido, pero tiene errores de sintaxis:

```json
{
  nombre: "Shopping Onelli",
  'abierto': True,
  "productos": ["alfajor", "Coca",]
}
```

- Detectar los tres errores sin ejecutar código, escribiéndolos como lista.
- Corregirlos y verificar que el resultado carga sin problemas con `json.loads()`.

> Pista: son los mismos tres errores típicos que aparecen en el apunte.

## Ejercicio 4: Recorrer y modificar

Usando el archivo `local.json` del apunte (`local`, `abierto`, `caja_actual`, `productos`):

- Recorrer la lista de `productos` e imprimir un mensaje `"<nombre>: quedan <stock> unidades"` por cada uno.
- Agregar un producto nuevo a la lista (por ejemplo `{"nombre": "agua", "precio": 800, "stock": 20}`).
- Restar 1 al `stock` de `"alfajores"`.
- Guardar los cambios en el mismo archivo, de forma que al volver a abrirlo con un editor de texto se vean reflejados.

> Ojo: si después de modificar `datos` no se vuelve a escribir el archivo, los cambios quedan solo en memoria.

## Ejercicio 5: `loads()` con datos "crudos"

Un sensor manda por red la siguiente lectura como un string (no como archivo):

```python
lectura = '{"ciudad": "Bariloche", "temperatura": 8.4, "viento": "Oeste 12", "sensacion_termica": null}'
```

- Convertir `lectura` a un diccionario de Python con la función que corresponda (¿`load` o `loads`?).
- Separar el campo `"viento"` en dos claves nuevas: `"direccion_viento"` y `"velocidad_viento"`.
- Armar un nuevo diccionario solo con los campos `ciudad`, `temperatura`, `direccion_viento` y `velocidad_viento`, y convertirlo de nuevo a JSON con `dumps(indent=2)`.

> Este ejercicio es un anticipo en chico de lo que va a pedir el proyecto con el archivo del SMN.
