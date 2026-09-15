# Módulo JSON

JSON (Javascript Object Notation) es un formato de texto usado para **guardar** y **compartir** datos estructurados dado a que es un estándar.

Suele aparecer cuando:

- un programa guarda información en un archivo;
- una app manda datos a otra;
- queremos dejar datos legibles para personas y programas.

> La mayoría de los sitios web maneja JSON para su comunicación con el navegador, por ejemplo cada vez que comparten un link las empresas comparten información del origen: (youtube, facebook, twitter, google, instagram, mercadolibre, etc..)

# Ejemplo archivo JSON

Notar el parecido a un diccionario. ¿Qué cosas difieren?

```json
{
    "local": "Shopping Onelli",
    "abierto": true,
    "caja_actual": null,
    "productos": [
        {
            "nombre": "alfajores", "precio": 1200, "stock": 14
        },
        {
            "nombre": "coca", "precio": 950, "stock": 9
        }
    ]
}
```

# Formato JSON

Es solo una cadena de texto (string) con reglas específicas de sintaxis, independiente de cualquier lenguaje.

Algunas cosas comparte con la sintaxis de diccionarios:

- Usa llaves `{}` para objetos.
- Usa corchetes `[]` para arrays.

y otras no:

- Las claves van entre comillas dobles.
- Aparecen `true`, `false` y `null`.
- Las comas separan elementos, pero no puede sobrar la última.

| Python | JSON |
|---|---|
| `list` | `array` |
| `None` | `null` |
| `True` / `False` | `true` / `false` |

- `tuple` y `list` Python json la convierte en un array JSON; al cargarla vuelve como `list`.
- `set` no se puede serializar directamente y produce `TypeError`.

# JSON válido vs JSON inválido

## Válido

```json
{
  "nombre": "Lisa",
  "activo": true
}
```

## Inválido

```json
{
  "nombre": 'Lisa',
  4: true,
}
```

Errores típicos:

- clave sin comillas;
- comillas simples;
- coma sobrante al final.

---

# Escribir JSON desde Python

El módulo `json` realiza una conversión automática basándose en la siguiente tabla de compatibilidad:

| Objeto en Python | Equivalente en JSON | Ejemplo |
| :--- | :--- | :--- |
| **`dict`** | `object` (Objeto) | `{"a": 1}` → `{"a": 1}` |
| **`list`**, **`tuple`** | `array` (Arreglo) | `[1, 2]` o `(1, 2)` → `[1, 2]` |
| **`str`** | `string` (Cadena) | `"Hola"` → `"Hola"` |
| **`int`**, **`float`** | `number` (Número) | `5`, `3.14` → `5`, `3.14` |
| **`True`** / **`False`** | `true` / `false` | `True` → `true` |
| **`None`** | `null` (Nulo) | `None` → `null` |

Vamos con ejemplos:

```python
import json

producto = {
    "nombre": "Coca",
    "precio": 950,
    "stock": 9
}

print(json.dumps(producto))
print(type(json.dumps(producto)))
```

`json.dumps()` recibe una estructura Python y la escribe como JSON. Devuelve un `string`, no imprime nada por sí solo — por eso el `print()`.

---

# Legibilidad de archivos JSON con `indent`

```python
import json

datos = {
    "local": "Shopping Onelli",
    "abierto": True,
    "productos": ["alfajor", "Coca"]
}

print(json.dumps(datos, indent=2))
```

Con `indent`, el archivo queda mucho más legible.

---

# Guardar JSON en un archivo

```python
import json

datos = {
    "local": "Shopping Onelli",
    "abierto": True,
    "productos": ["alfajor", "Coca"]
}
with open('local.json', 'w') as file:
    json.dump(datos, file, indent=2)
```

`json.dump()` (sin la *s*) recibe una estructura Python y la escribe como JSON en un archivo.

---

# Volver a cargar datos

```python
import json

with open("local.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)
print(type(datos))
```

`json.load()` lee el archivo JSON y devuelve estructuras de Python.

---

# Leer, recorrer y modificar

Los objetos JSON, una vez cargados, son iterables como cualquier diccionario o lista de Python:

```python
import json

with open("local.json", "r") as archivo:
    datos = json.load(archivo)

for producto in datos["productos"]:
    print(producto)

datos["abierto"] = False
datos["caja_actual"] = "caja_2"
```

Después de `load()`, volvemos a tener listas, diccionarios y valores de Python.

Si se quiere que el cambio quede guardado en el archivo, hay que volver a escribirlo:

```python
with open("local.json", "w") as archivo:
    json.dump(datos, archivo, indent=2)
```

---

# `json.loads()`: parsear un string en vez de un archivo

A veces los datos no vienen de un archivo sino de un string (por ejemplo, texto recibido de otro programa o ya leído previamente). Para eso está `json.loads()` (con *s*, de *string*):

```python
import json

texto = '{"nombre": "Coca", "precio": 950, "stock": 9}'

producto = json.loads(texto)
print(producto)
print(type(producto))
```

| Función | Fuente/destino | Uso |
| :--- | :--- | :--- |
| `json.load()` | archivo | leer JSON desde un archivo abierto |
| `json.loads()` | string | leer JSON desde un string ya en memoria |
| `json.dump()` | archivo | escribir JSON a un archivo abierto |
| `json.dumps()` | string | convertir a JSON como string |

La regla mnemotécnica: la *s* final es de *string*; sin *s* es archivo.
